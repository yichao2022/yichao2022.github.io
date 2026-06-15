#!/usr/bin/env python3
"""
USD/CNY Technical Analysis
- 拉取5年历史汇率数据 (Yahoo Finance CNY=X, 直接就是USD/CNY)
- 计算关键均线、波动率、趋势信号
- 输出简洁报告
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys

TICKER = "CNY=X"
LOOKBACK_YEARS = 5


def fetch_data(years=LOOKBACK_YEARS):
    end = datetime.now()
    start = end - timedelta(days=years * 365)
    df = yf.download(TICKER, start=start, end=end, progress=False)
    if df.empty:
        print("❌ 无法获取数据，请检查网络或 ticker")
        sys.exit(1)
    # Yahoo Finance CNY=X returns Close as a MultiIndex DataFrame
    # Extract the actual close prices
    close = df["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]  # Take first (and only) column
    df["price"] = close
    return df


def compute_metrics(df):
    price = df["price"]
    latest = float(price.iloc[-1])
    prev_close = float(price.iloc[-2])

    # Moving averages
    ma20 = float(price.rolling(20).mean().iloc[-1])
    ma50 = float(price.rolling(50).mean().iloc[-1])
    ma200 = float(price.rolling(200).mean().iloc[-1])

    # Volatility (20-day annualized)
    daily_returns = price.pct_change().dropna()
    vol_20d = float(daily_returns.tail(20).std() * np.sqrt(252))

    # 52-week high/low
    year_data = price.tail(252)
    high_52w = float(year_data.max())
    low_52w = float(year_data.min())

    # Distance from MA200
    pct_from_ma200 = (latest / ma200 - 1) * 100

    # RSI (14-day)
    delta = daily_returns.tail(15)
    gain = float(delta.where(delta > 0, 0).sum())
    loss = float((-delta.where(delta < 0, 0)).sum())
    rsi = 100 - (100 / (1 + gain / loss)) if loss != 0 else 100

    # Support / Resistance
    support = round(latest * 0.97, 2)
    resistance = round(latest * 1.03, 2)

    return {
        "latest": latest,
        "prev_close": prev_close,
        "change_pct": (latest / prev_close - 1) * 100,
        "ma20": ma20,
        "ma50": ma50,
        "ma200": ma200,
        "vol_20d": vol_20d,
        "high_52w": high_52w,
        "low_52w": low_52w,
        "pct_from_ma200": pct_from_ma200,
        "rsi": rsi,
        "support": support,
        "resistance": resistance,
    }


def signal_strength(m):
    signals = 0
    reasons = []

    if m["latest"] > m["ma50"]:
        signals += 1
        reasons.append(f"价格在MA50上方 (+1)")
    else:
        signals -= 1
        reasons.append(f"价格在MA50下方 (-1)")

    if m["latest"] > m["ma200"]:
        signals += 1
        reasons.append(f"价格在MA200上方 (+1)")
    else:
        signals -= 1
        reasons.append(f"价格在MA200下方 (-1)")

    if m["rsi"] > 70:
        signals -= 1
        reasons.append(f"RSI {m['rsi']:.0f} > 70, 超买回调风险 (-1)")
    elif m["rsi"] < 30:
        signals += 1
        reasons.append(f"RSI {m['rsi']:.0f} < 30, 超卖反弹可能 (+1)")

    return signals, reasons


def print_report(df, m, sig, reasons):
    r = m["latest"]

    print("=" * 58)
    print("         USD/CNY 技术分析报告")
    print(f"         数据截至: {df.index[-1].strftime('%Y-%m-%d')}")
    print("=" * 58)

    print(f"\n📊 当前价格")
    print(f"   USD/CNY:   {r:.4f}")
    print(f"   日变化:    {m['change_pct']:+.2f}%")
    print(f"   52周最高:  {m['high_52w']:.4f}")
    print(f"   52周最低:  {m['low_52w']:.4f}")

    print(f"\n📈 均线")
    above_below = lambda v: "▲ 上方" if r > v else "▼ 下方"
    print(f"   MA20  ({m['ma20']:.4f})  — 价格在{above_below(m['ma20'])}")
    print(f"   MA50  ({m['ma50']:.4f})  — 价格在{above_below(m['ma50'])}")
    print(f"   MA200 ({m['ma200']:.4f})  — 价格在{above_below(m['ma200'])}")
    print(f"   距MA200: {m['pct_from_ma200']:+.2f}%")

    print(f"\n📉 波动率 & 动量")
    print(f"   20日年化波动率: {m['vol_20d']*100:.2f}%")
    rsi_label = "超买" if m["rsi"] > 70 else "超卖" if m["rsi"] < 30 else "中性"
    print(f"   RSI(14):        {m['rsi']:.1f}  ({rsi_label})")

    print(f"\n🛡️ 关键点位")
    print(f"   短期支撑: {m['support']:.4f}  (-3%)")
    print(f"   短期阻力: {m['resistance']:.4f}  (+3%)")

    print(f"\n🔍 综合信号")
    if sig > 0:
        direction = "🟢 看多美元 (USD/CNY ↑)"
    elif sig < 0:
        direction = "🔴 看空美元 (USD/CNY ↓)"
    else:
        direction = "⚪ 中性"
    print(f"   信号强度: {sig:+d} → {direction}")
    for r_text in reasons:
        print(f"   • {r_text}")

    print(f"\n💡 换汇建议（人民币→美元）")
    if r >= 7.0:
        print(f"   当前 {r:.2f} ≥ 7.0")
        print(f"   → ⚠️ 人民币弱，买1美元要花{r:.2f}元，成本高")
        print(f"   建议：等回调，不急于换")
    elif r <= 6.5:
        print(f"   当前 {r:.2f} ≤ 6.5")
        print(f"   → ✅ 人民币强，买1美元只要{r:.2f}元，划算")
        print(f"   建议：可以考虑锁定汇率")
    else:
        print(f"   当前 {r:.2f} 在6.5-7.0中性区间")
        print(f"   建议：小额分批换，不择时")

    recent = df.tail(30)
    trend_val = float(recent["price"].iloc[-1]) - float(recent["price"].iloc[0])
    trend_dir = "↑ 上涨" if trend_val > 0 else "↓ 下跌"
    print(f"\n📅 近30天: {trend_dir}  ({float(recent['price'].iloc[0]):.4f} → {float(recent['price'].iloc[-1]):.4f})")

    print("\n" + "=" * 58)
    print(f"   cd ~/yichao2022_repo && python3 usdcny_analysis.py")
    print("=" * 58)


if __name__ == "__main__":
    print("正在获取 USD/CNY 数据...")
    df = fetch_data()
    m = compute_metrics(df)
    sig, reasons = signal_strength(m)
    print_report(df, m, sig, reasons)
