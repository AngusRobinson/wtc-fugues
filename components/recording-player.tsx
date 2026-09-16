import type {FugueData} from '@/lib/fugues/types';

export function RecordingPlayer({recording}:{recording:NonNullable<FugueData['recording']>}){
 const {youtubeId,startSeconds,performer,instrument,source}=recording;
 return <aside className="recording-panel" aria-label="NBS performance">
  <iframe title={performer+' — '+instrument+' — Netherlands Bach Society'}
   src={'https://www.youtube-nocookie.com/embed/'+youtubeId+'?start='+startSeconds+'&autoplay=0&playsinline=1&rel=0'}
   width="360" height="203" allow="encrypted-media; fullscreen; picture-in-picture" allowFullScreen
   referrerPolicy="strict-origin-when-cross-origin"/>
  <p className="recording-performer">{performer}<span>{instrument}</span></p>
  <div className="recording-links"><a href={source.href} target="_blank" rel="noreferrer">{source.label}</a><a href={'https://www.youtube.com/watch?v='+youtubeId+'&t='+startSeconds+'s'} target="_blank" rel="noreferrer">YouTube ↗</a></div>
 </aside>;
}
