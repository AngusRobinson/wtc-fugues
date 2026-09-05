import {notFound} from 'next/navigation';
import FugueStudy from '@/components/fugue-study';
import {catalogue,loadStudy} from '@/lib/fugues/catalogue';

export function generateStaticParams(){return catalogue.map(work=>({id:work.id}));}
export async function generateMetadata({params}:{params:Promise<{id:string}>}){
 const {id}=await params,work=catalogue.find(work=>work.id===id);
 if(!work)notFound();
 return {title:work.title+' · BWV '+work.bwv,description:work.description};
}
export default async function FuguePage({params}:{params:Promise<{id:string}>}){
 const {id}=await params,study=await loadStudy(id);
 if(!study)notFound();
 return <FugueStudy key={id} study={study} collectionHref="../../"/>;
}
