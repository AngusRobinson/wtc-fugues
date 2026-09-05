import type {WorkMetadata} from '@/lib/fugues/types';

export default function FugueCatalogue({works,offline=false}:{works:WorkMetadata[];offline?:boolean}) {
 return <main className="fugue-catalogue">
  <header><p>J. S. Bach</p><h1>The Well-Tempered Clavier</h1><p>Fugue analyses</p></header>
  {[1,2].map(book=>{
   const entries=works.filter(work=>work.book===book);
   return entries.length>0&&<section key={book}><h2>Book {book===1?'I':'II'}</h2>
    <ul>{entries.map(work=><li key={work.id}>
     <a href={`./fugues/${work.id}/${offline?'index.html':''}`}>No. {work.number} · {work.key} <span>BWV {work.bwv}</span></a>
    </li>)}</ul>
   </section>;
  })}
 </main>;
}
