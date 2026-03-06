# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### HR & Administrative Contacts
- **USC HR Service Center**: uschr@usc.edu | (213) 821-8100 (For Schaeffer Center follow-ups).
- **File Transfer (Telegram)**: If direct links fail, use the CLI: `openclaw message send --channel telegram --target 8573621578 --media <absolute_path> --message "<text>"`.
- **Target ID**: 8573621578 (Telegram).

### Web Scraping & Search (Priority)
1. **Bright Data**: Primary engine for `web_search` and `fetch`. High success rate, uses residential IPs (5,000 free requests/mo).
2. **Nanobrowser**: Primary for form-filling and site-specific navigation in Chrome sidebar.
3. **Firecrawl**: Secondary defense/fallback for extreme anti-bot (Cloudflare/Captchas).
4. **agent-browser**: Local fallback for basic university sites.

### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
