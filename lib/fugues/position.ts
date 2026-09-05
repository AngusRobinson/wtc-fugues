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
 return bar.number+':'+String(beat).replace('.5','½').replace('.25','¼').replace('.75','¾');
}
