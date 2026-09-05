import fs from 'node:fs';
import path from 'node:path';
import {escapeHtml} from './catalogue.mjs';
export function packageHtml(build,work){
let html=fs.readFileSync(path.join(build,'index.html'),'utf8');
html=html.replace(/<link\b[^>]*rel="stylesheet"[^>]*>/g,tag=>{
 const ref=tag.match(/href="([^"]+)"/)?.[1];if(!ref)throw new Error('Missing stylesheet path');
 const css=fs.readFileSync(path.resolve(build,ref),'utf8');
 return '<style>'+css+'</style>';
});
html=html.replace(/<script\b[^>]*src="([^"]+)"[^>]*><\/script>/g,(_tag,ref)=>{
 const js=fs.readFileSync(path.resolve(build,ref),'utf8').replace(/<\/script/gi,'<\\/script');
 return '<script type="module">'+js+'</script>';
});
html=html.replace(/<link\b[^>]*rel="modulepreload"[^>]*>/g,'');
html=html.replace('<div id="root"></div>','<div id="root"></div><noscript><p>This interactive musical study needs JavaScript enabled in your browser.</p></noscript>');
if(/<(?:script|link)\b[^>]*(?:src|href)="\.\/assets\//.test(html))throw new Error('An external build asset remains.');
return html.replace('__WORK_TITLE__',escapeHtml(work.title+' · BWV '+work.bwv)).replace('__WORK_DESCRIPTION__',escapeHtml(work.description));
}
