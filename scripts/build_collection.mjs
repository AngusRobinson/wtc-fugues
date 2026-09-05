import fs from 'node:fs';
import path from 'node:path';
import {build as viteBuild} from 'vite';
import {build as bundle} from 'esbuild';
import React from 'react';
import {renderToStaticMarkup} from 'react-dom/server';
import {readCatalogue,syncRegistry,copyPublicFiles,root} from './catalogue.mjs';
import {packageHtml} from './package_html.mjs';

const works=readCatalogue();syncRegistry(works);
const site=path.join(root,'output/site');fs.mkdirSync(site,{recursive:true});
for(const work of works){
 process.env.FUGUE_ID=work.id;
 await viteBuild({configFile:path.join(root,'vite.standalone.config.ts')});
 const html=packageHtml(path.join(root,'output/browser-build'),work);
 const destination=path.join(site,'fugues',work.id);fs.mkdirSync(destination,{recursive:true});
 fs.writeFileSync(path.join(destination,'index.html'),html);
 copyPublicFiles(work,destination);
 copyPublicFiles(work,path.join(root,'public/fugues',work.id));
 const legacyHtml=html.replace('data-collection-href="../../index.html"','data-collection-href="./site/index.html"');
 for(const name of work.legacyPages??[])fs.writeFileSync(path.join(root,'output',name),legacyHtml);
 if(work.legacyPages?.length){
  for(const file of work.publicFiles.filter(f=>f.startsWith('pdf/'))){
   const target=path.join(root,'output',file);fs.mkdirSync(path.dirname(target),{recursive:true});
   fs.copyFileSync(path.join(destination,file),target);
  }
 }
}
delete process.env.FUGUE_ID;
fs.mkdirSync(path.join(root,'tmp/checks'),{recursive:true});
await bundle({entryPoints:[path.join(root,'components/fugue-catalogue.tsx')],bundle:true,packages:'external',platform:'node',format:'esm',outfile:path.join(root,'tmp/checks/catalogue-render.mjs')});
const {default:Catalogue}=await import('../tmp/checks/catalogue-render.mjs');
const css=fs.readFileSync(path.join(root,'app/collection.css'),'utf8');
const markup=renderToStaticMarkup(React.createElement(Catalogue,{works,offline:true}));
fs.writeFileSync(path.join(site,'index.html'),`<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Bach: The Well-Tempered Clavier · Fugue analyses</title><style>body{margin:0;background:white}${css}</style></head><body>${markup}</body></html>\n`);
console.log(`Built ${works.length} standalone fugue(s) and the collection index in output/site.`);
