import FugueCatalogue from '@/components/fugue-catalogue';
import {catalogue} from '@/lib/fugues/catalogue';
export default function Home() { return <FugueCatalogue works={catalogue}/>; }
