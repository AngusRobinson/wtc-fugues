"""Compare the rendered MIDI's complete pitch/onset multiset with the source events."""
from collections import Counter
import base64,struct

def verify_midi(toolkit,events):
 data=base64.b64decode(toolkit.renderToMIDI());assert data[:4]==b'MThd'
 hlen=struct.unpack('>I',data[4:8])[0];division=struct.unpack('>H',data[12:14])[0]
 assert division<0x8000
 pos=8+hlen;onsets=[]
 while pos<len(data):
  assert data[pos:pos+4]==b'MTrk';size=struct.unpack('>I',data[pos+4:pos+8])[0];track=data[pos+8:pos+8+size];pos+=8+size
  i=0;tick=0;running=None
  def vlq():
   nonlocal i
   value=0
   while True:
    byte=track[i];i+=1;value=(value<<7)|(byte&127)
    if not byte&128:return value
  while i<len(track):
   tick+=vlq();status=track[i]
   if status&128:i+=1
   else:assert running is not None;status=running
   if status==255:
    i+=1;n=vlq();i+=n;continue
   if status in (240,247):n=vlq();i+=n;continue
   assert 128<=status<240,status
   running=status;kind=status>>4;length=1 if kind in (12,13) else 2;args=track[i:i+length];i+=length
   if kind==9 and args[1]>0:onsets.append((args[0],round(tick/division,6)))
 expected=Counter((e['pitch'],round(e['start'],6)) for e in events if not e['tied'])
 actual=Counter(onsets)
 if actual!=expected:
  # SMF timestamps are integer ticks. Verovio may floor a triplet by one tick.
  # Compare all attacks within the format's resolution, retaining pitch and multiplicity.
  for pitch in {p for p,q in expected}|{p for p,q in actual}:
   want=sorted(q for (p,q),count in expected.items() if p==pitch for _ in range(count))
   got=sorted(q for (p,q),count in actual.items() if p==pitch for _ in range(count))
   assert len(want)==len(got),(pitch,len(want),len(got))
   assert all(abs(a-b)<=1/division+1e-6 for a,b in zip(want,got)),(pitch,[(a,b) for a,b in zip(want,got) if abs(a-b)>1/division+1e-6][:8])
 # The timemap independently retains onset identities, including unisons.
 on={ident:entry['qstamp'] for entry in toolkit.renderToTimemap() for ident in entry.get('on',[])}
 for e in events:
  if not e['tied']:assert e['id'] in on and abs(on[e['id']]-e['start'])<1e-6,(e,on.get(e['id']))
 return len(onsets)
