import fs from 'node:fs/promises';
import sharp from 'sharp';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const work=fileURLToPath(new URL('../',import.meta.url));
const directory=path.resolve(work,'../../../tmp',path.basename(work),'pdfs');
const systems=JSON.parse(await fs.readFile(path.join(work,'data/annotated-systems.json'),'utf8'));
await fs.mkdir(directory,{recursive:true});
for(const s of systems){
 await sharp(Buffer.from(s.svg)).resize({width:4400}).flatten({background:'#ffffff'}).png().toFile(path.join(directory,`system-${s.start}.png`));
}
console.log(`Prepared ${systems.length} score systems at 600 dpi.`);
