import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import sharp from 'sharp';
const directory=fileURLToPath(new URL('../../../../tmp/wtc-i-23/',import.meta.url));
for(const mode of ['open','keyboard']){
 const systems=JSON.parse(await fs.readFile(`${directory}/${mode}-systems.json`,'utf8'));
 for(const s of systems)await sharp(Buffer.from(s.svg)).resize(4200).flatten({background:'#fff'}).png().toFile(`${directory}/${mode}-${s.start}.png`);
}
console.log('Prepared 18 score systems for print.');
