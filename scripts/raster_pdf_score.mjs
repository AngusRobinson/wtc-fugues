/** Rasterise a PDF-specific score SVG supplied on stdin. */
import fs from 'node:fs';
import sharp from 'sharp';
const output=process.argv[2];
if(!output)throw new Error('Output PNG path required');
await sharp(fs.readFileSync(0)).resize(4400).flatten({background:'#fff'}).png().toFile(output);
