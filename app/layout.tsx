import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata = { title: 'Bach: The Well-Tempered Clavier · Fugue analyses', description: 'Analyses and annotated scores of fugues from both books of The Well-Tempered Clavier.' };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en-GB"><body>{children}</body></html>; }
