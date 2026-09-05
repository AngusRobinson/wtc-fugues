import React from 'react';
import {createRoot} from 'react-dom/client';
import FugueStudy from '../components/fugue-study';
import study from '@study';
import '../styles/globals.css';
createRoot(document.getElementById('root')!).render(<FugueStudy study={study} collectionHref={document.body.dataset.collectionHref}/>);
