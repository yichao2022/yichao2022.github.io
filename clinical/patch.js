const fs = require('fs');

const htmlPath = '/Users/cary/.openclaw/workspace/yichao2022.github.io/clinical/index.html';
const injectionPath = '/Users/cary/.openclaw/workspace/yichao2022.github.io/clinical/synthetic_chart_injection.txt';

let html = fs.readFileSync(htmlPath, 'utf8');
const injection = fs.readFileSync(injectionPath, 'utf8');

if (!html.includes('Synthetic Dashboard Section')) {
    html = html.replace('</main>', '\n' + injection + '\n    </main>');
    fs.writeFileSync(htmlPath, html);
    console.log('Injection successful');
} else {
    console.log('Already injected');
}