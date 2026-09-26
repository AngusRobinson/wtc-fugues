import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
const require=createRequire(process.env.WTC_PACKAGE_JSON??new URL('../../../../package.json',import.meta.url));
const sharp=require('sharp');
const directory=process.env.WTC_PDF_TMP??fileURLToPath(new URL('../../../../tmp/wtc-i-15/',import.meta.url));
for(const mode of ['open','keyboard']){
 const systems=JSON.parse(await fs.readFile(`${directory}/${mode}-systems.json`,'utf8'));
 for(const s of systems)await sharp(Buffer.from(s.svg)).resize(4200).flatten({background:'#fff'}).png().toFile(`${directory}/${mode}-${s.start}.png`);
}
console.log('Prepared 44 score systems for print.');
