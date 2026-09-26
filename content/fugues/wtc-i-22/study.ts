import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 recording:{"youtubeId": "rbcYLQZouiM", "startSeconds": 162, "performer": "Kris Verhelst", "instrument": "Harpsichord", "source": {"label": "Netherlands Bach Society", "href": "https://www.bachvereniging.nl/en/bwv/bwv-867"}},
 metadata,voices:voices.map((name,i)=>({name,short:["SI", "SII", "A", "T", "B"][i]})),
 bars:Array.from({length:75},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:2})),
 tempo:{"initial": 52, "min": 36, "max": 92, "beatQuarters": 2, "label": "Minim"},initialLoop:[1,6],initialTone:"db25",seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{"id": "subject", "label": "Subject / answer", "colour": "#244f91", "role": "subject"}, {"id": "motif", "label": "Derived figures", "colour": "#637878", "role": "cell"}, {"id": "head", "label": "Subject-head allusions", "colour": "#637878", "role": "cell"}, {"id": "sequence", "label": "Sequential figure", "colour": "#8a6548", "role": "cell"}],
 annotations:annotated.annotations,
 notes:{
  "examples": "",
  "formal": "Two parts, following Keller.",
  "formalSource": {
    "label": "Keller, pp. 108–110.",
    "href": "https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv867.pdf#page=2"
  },
  "map": "◆ Harmonic arrival · ○ Entry context. Beats are minims.",
  "disposition": "Positions use bar:beat.",
  "notation": "S subject · A tonal answer · * varied / incomplete · > continuation",
  "cells": "d descending crotchet figure · di its inversion · h* head allusion · q sequential quaver figure",
  "edition": [
    "Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Thematic spans and harmonic markers are editorial readings checked against the score, Keller, Prout and Tovey. Playback joins ties and omits ornaments.",
    "The overview follows Keller’s division at the A♭ cadence in 37; bar references are checked against the 75-bar score, including the bass entry at 15 (printed as 18 in Keller). Voice names follow the Kroll/Huron allocation. Tovey redistributes some inner parts: the entries labelled soprano II at 37 and alto at 46 here are alto and tenor in his reading. Subject spans retain the full continuation where recognisable; shortened and altered entries are marked with an asterisk."
  ],
  "scoreSource": {
    "label": "Score source",
    "href": "https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f22.krn"
  }
}
};
export default study;
