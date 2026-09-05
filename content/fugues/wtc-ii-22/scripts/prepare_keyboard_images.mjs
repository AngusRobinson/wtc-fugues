import fs from 'node:fs/promises';
import sharp from 'sharp';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const work=fileURLToPath(new URL('../',import.meta.url));
const directory=path.resolve(work,'../../../tmp',path.basename(work),'pdfs/keyboard');
const systems=JSON.parse(await fs.readFile(directory+'/systems.json','utf8'));
for(const system of systems){
 await sharp(Buffer.from(system.svg)).resize(4400).flatten({background:'#fff'}).png().toFile(`${directory}/system-${system.start}.png`);
}
console.log(`Prepared ${systems.length} keyboard systems.`);
