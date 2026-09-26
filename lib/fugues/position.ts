import type {Bar,ScoreSystem} from './types';

export function barAt(bars:Bar[],q:number):Bar {
 return bars.find(b=>q>=b.start&&q<b.start+b.duration)??(q<bars[0].start?bars[0]:bars[bars.length-1]);
}
export function barStart(bars:Bar[],number:number):number {
 const bar=bars.find(b=>b.number===number);
 if(!bar)throw new Error('Unknown bar: '+number);
 return bar.start;
}
export function barEnd(bars:Bar[],number:number):number {
 const bar=bars.find(b=>b.number===number);
 if(!bar)throw new Error('Unknown bar: '+number);
 return bar.start+bar.duration;
}
export function systemAt(systems:ScoreSystem[],bar:number):number {
 return systems.findIndex(s=>bar>=s.start&&bar<=s.end);
}
export function scorePosition(bars:Bar[],q:number):string {
 const bar=barAt(bars,q),beat=1+(q-bar.start)/bar.beatQuarters;
 const whole=Math.floor(beat+1e-8),fraction=beat-whole;
 const fractions:[[number,string],...Array<[number,string]>]=[[0,''],[1/6,'⅙'],[.25,'¼'],[1/3,'⅓'],[.5,'½'],[2/3,'⅔'],[.75,'¾'],[5/6,'⅚']];
 const match=fractions.find(([value])=>Math.abs(fraction-value)<1e-8);
 return bar.number+':'+(match?String(whole)+match[1]:String(Number(beat.toFixed(3))));
}
