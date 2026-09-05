import {defineConfig} from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/postcss';
import {fileURLToPath} from 'node:url';
import {readCatalogue} from './scripts/catalogue.mjs';
const workId=process.env.FUGUE_ID??readCatalogue()[0]?.id;
if(!readCatalogue().some((work:{id:string})=>work.id===workId))throw new Error('Unknown fugue: '+workId);
export default defineConfig({
 root:'standalone',base:'./',
 publicDir:false,
 resolve:{alias:{'@':fileURLToPath(new URL('.',import.meta.url)),'@study':fileURLToPath(new URL(`./content/fugues/${workId}/study.ts`,import.meta.url))}},
 css:{postcss:{plugins:[tailwindcss()]}},
 plugins:[react()],
 build:{outDir:'../output/browser-build',emptyOutDir:true,assetsInlineLimit:10000000,
 rolldownOptions:{output:{codeSplitting:false}}},
});
