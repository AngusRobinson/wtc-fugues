import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import sharp from 'sharp';
const work=fileURLToPath(new URL('../',import.meta.url));
const directory=path.resolve(work,'../../../tmp',path.basename(work));
for(const mode of ['open','keyboard']){
 const systems=JSON.parse(await fs.readFile(path.join(directory,mode+'-systems.json'),'utf8'));
 for(const system of systems)await sharp(Buffer.from(system.svg)).resize(4400).flatten({background:'#fff'}).png().toFile(path.join(directory,`${mode}-${system.start}.png`));
}
console.log('Prepared 16 score systems for print.');
