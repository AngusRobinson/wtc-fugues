import path from 'node:path';
import {readCatalogue,syncRegistry,copyPublicFiles,root} from './catalogue.mjs';
const works=readCatalogue();
syncRegistry(works);
for(const work of works)copyPublicFiles(work,path.join(root,'public/fugues',work.id));
console.log(`Prepared catalogue and public documents for ${works.length} fugue(s).`);
