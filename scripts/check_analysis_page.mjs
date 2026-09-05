import {build} from 'esbuild';
import fs from 'node:fs';
import assert from 'node:assert/strict';
import React from 'react';
import {renderToStaticMarkup} from 'react-dom/server';
fs.mkdirSync('tmp/checks',{recursive:true});
await build({stdin:{contents:"export {default} from './components/fugue-study';export {default as study} from './content/fugues/wtc-ii-22/study';",resolveDir:process.cwd(),loader:'tsx'},bundle:true,packages:'external',platform:'node',format:'esm',alias:{'@':process.cwd()},outfile:'tmp/checks/render-check.mjs'});
const {default:Study,study}=await import('../tmp/checks/render-check.mjs');
const html=renderToStaticMarkup(React.createElement(Study,{study}));
fs.writeFileSync('tmp/checks/render-check.html',html);
const ids=[...html.matchAll(/\sid="([^"]+)"/g)].map(x=>x[1]);
assert.equal(new Set(ids).size,ids.length,'Duplicate SVG/HTML identifiers');
assert(html.indexOf('id="themes-title"')<html.indexOf('id="map-title"'));
assert(html.indexOf('id="map-title"')<html.indexOf('id="complete-score"'));
assert.equal((html.match(/class="theme-example"/g)||[]).length,3);
assert.equal((html.match(/aria-label="Score, bars /g)||[]).length,25);
assert.equal((html.match(/class="tonal-marker /g)||[]).length,17);
assert.equal((html.match(/data-note-id=/g)||[]).length,1828);
assert(html.includes('<details class="disposition" open=""'));
for(const name of ['output/bach-bflat-minor-fugue.html','output/bach-bflat-minor-fugue-analysis.html']){
 const packed=fs.readFileSync(name,'utf8');assert(!/<script[^>]+src=/.test(packed));assert(!/<link[^>]+(?:stylesheet|preload)/.test(packed));
}
assert.equal(fs.readFileSync('output/bach-bflat-minor-fugue.html','utf8'),fs.readFileSync('output/bach-bflat-minor-fugue-analysis.html','utf8'));
assert(fs.existsSync('output/pdf/bach-bflat-minor-fugue-annotated.pdf'));
assert(fs.existsSync('output/pdf/bach-bflat-minor-fugue-keyboard.pdf'));
console.log('Checked: thematic-first order; three examples; 17 tonal markers; 25 systems; 1,828 notes; unique identifiers; offline packaging; both filenames updated.');
