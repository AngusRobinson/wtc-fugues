import type {FugueData} from '@/lib/fugues/types';
import metadata from './metadata.json';
import {events,audio,duration} from './data/score.json';
import systems from './data/annotated-systems.json';
import annotated from './data/annotations.json';
import examples from './data/thematic-examples.json';
import {voices,formalGroups,sections,themes,tonalEvents} from './analysis';
const study:FugueData={
 recording:{"youtubeId": "xCqWH9bKzQE", "startSeconds": 134, "performer": "Siebe Henstra", "instrument": "Harpsichord", "source": {"label": "Netherlands Bach Society", "href": "https://www.bachvereniging.nl/en/bwv/bwv-846"}},
 metadata,voices:voices.map((name,i)=>({name,short:["S", "A", "T", "B"][i]})),
 bars:Array.from({length:27},(_,i)=>({number:i+1,start:i*4,duration:4,beatQuarters:1})),
 tempo:{"initial": 56, "min": 36, "max": 92, "beatQuarters": 1, "label": "Crotchet"},initialLoop:[1,4],initialTone:"a14",seekStep:.25,
 score:{events,audio,duration},systems,examples,formalGroups,sections,themes,tonalEvents,
 materials:[{"id": "subject", "label": "Subject / answer", "colour": "#244f91", "role": "subject"}, {"id": "motif", "label": "Derived figures", "colour": "#637878", "role": "cell"}, {"id": "head", "label": "Subject-head allusions", "colour": "#637878", "role": "cell"}],
 annotations:annotated.annotations,
 notes:{
  "examples": "",
  "formal": "Two parts, following Keller.",
  "formalSource": {
    "label": "Keller, pp. 41–44.",
    "href": "https://www.hermann-keller.org/assets/downloads/547e2aeb/bwv846.pdf#page=3"
  },
  "map": "◆ Harmonic arrival · ○ Entry context. Beats are crotchets.",
  "disposition": "Positions use bar:beat.",
  "notation": "S subject · A real answer · * varied / incomplete · > continuation",
  "cells": "d descending semiquaver figure · di its inversion · h* head allusion",
  "edition": [
    "Kroll, Bach-Gesellschaft XIV (1866); Humdrum encoding by David Huron, revised by Craig Sapp. Thematic spans and harmonic markers are editorial readings checked against the score, Keller, Prout and Tovey. Playback joins ties and omits ornaments.",
    "Keller’s two-part division at the A minor cadence governs the overview. Prout separates a counter-exposition and a final section at 24. The twenty-four entry spans include curtailed statements; the further head allusions at 16, 20 and 24 are marked separately. The score retains the primary Kroll reading of the encoded ossias in bars 4, 8 and 12; Tovey adopts different readings at 4 and 9."
  ],
  "scoreSource": {
    "label": "Score source",
    "href": "https://github.com/humdrum-tools/bach-wtc-fugues/blob/master/kern/wtc1f01.krn"
  }
}
};
export default study;
