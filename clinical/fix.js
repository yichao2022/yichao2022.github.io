const fs = require('fs');
let html = fs.readFileSync('/Users/cary/.openclaw/workspace/yichao2022.github.io/clinical/index.html', 'utf8');

// Replace module script with regular script
html = html.replace('<script type="module">', '<script>');
html = html.replace("import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';", '');

// Add mermaid script tag before the main script
html = html.replace('<!-- Marked.js for Markdown parsing -->', 
`<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.0/dist/mermaid.min.js"></script>
    <!-- Marked.js for Markdown parsing -->`);

fs.writeFileSync('/Users/cary/.openclaw/workspace/yichao2022.github.io/clinical/index.html', html);
