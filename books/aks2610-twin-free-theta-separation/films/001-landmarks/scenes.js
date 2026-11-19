'use strict';

// Authored scenes use the installed film engine; no separate player or runtime.
FILM.hud = false;
const mapNodes = [
  {id:'u',x:250,y:440},{id:'v',x:1180,y:440},
  {id:'a',x:560,y:240},{id:'b',x:870,y:240},
  {id:'c',x:560,y:440},{id:'d',x:870,y:440},
  ...Array.from({length:9},(_,i)=>({id:`y${i+1}`,x:250+930*(i+1)/10,y:440+270*Math.sin(Math.PI*(i+1)/10)}))
];
const mapEdges = [['u','a'],['a','b'],['b','v'],['u','c'],['c','d'],['d','v'],
  ...Array.from({length:10},(_,i)=>[i===0?'u':`y${i}`,i===9?'v':`y${i+1}`])];
const byName = Object.fromEntries(mapNodes.map(n=>[n.id,n]));
function distances(start) {
  const d = {[start]:0}, queue=[start];
  for (let i=0;i<queue.length;i++) for (const [a,b] of mapEdges) {
    const next = a===queue[i]?b:b===queue[i]?a:null;
    if (next && d[next]===undefined) {d[next]=d[queue[i]]+1;queue.push(next);}
  }
  return d;
}
const fromA=distances('a'),fromY1=distances('y1');
const distinctAddresses=new Set(mapNodes.map(n=>`${fromA[n.id]},${fromY1[n.id]}`)).size;
if (distinctAddresses!==15) throw new Error('The displayed landmark example must have fifteen distinct addresses');
function paperFrame(title,zh) {
  fillBox(0,0,W,H,C.bg,1);
  txt(title,120,135,{size:48,fam:F.disp,w:700});
  txt(zh,120,190,{size:31,fam:F.zh,c:C.dim});
}
function graph(a,pattern=false) {
  for (const [left,right] of mapEdges) {
    const p=byName[left],q=byName[right];
    line(p.x,p.y,q.x,q.y,C.dim,a,3);
  }
  const values={a:1,b:1,c:-1,d:-1};
  for (const n of mapNodes) {
    const landmark=!pattern&&(n.id==='a'||n.id==='y1');
    const color=landmark?C.now:pattern&&values[n.id]===-1?C.mag:C.cyan;
    ctx.save();ctx.globalAlpha=a;ctx.fillStyle=C.bg;
    ctx.beginPath();ctx.arc(n.x,n.y,pattern?20:11,0,TAU);ctx.fill();ctx.restore();
    ring(n.x,n.y,pattern?20:11,color,a,3);
    if (pattern) txt(String(values[n.id]||0),n.x,n.y+7,{size:23,fam:F.math,align:'center',c:color,a});
    if (['u','v','a','b','c','d','y1','y5','y9'].includes(n.id))
      txt(n.id.replace('y','y'),n.x,n.y-(pattern?31:22),{size:23,fam:F.mono,align:'center',a,c:landmark?C.now:C.white});
  }
}

SCENES.landmarks = S => {
  paperFrame('Can two distances tell you where you are?','两个距离，能确定你在哪里吗？');
  graph(clamp(S.u/0.8));
  const a=at(S,1,0.8);
  txt('LANDMARKS',1330,310,{size:25,fam:F.mono,c:C.now,a});
  txt('a and y1',1330,365,{size:37,fam:F.mono,a});
  txt('Distance address',1330,445,{size:30,fam:F.disp,a});
  ['a : (0, 2)','y1: (2, 0)','y9: (3, 5)'].forEach((s,i)=>txt(s,1330,500+i*55,{size:32,fam:F.mono,a}));
  txt(`${distinctAddresses} different pairs`,1330,710,{size:30,fam:F.disp,c:C.now,a});
  txt('Two 3-edge routes and one 10-edge route: 15 vertices',250,815,{size:29,fam:F.disp,c:C.dim});
};

SCENES.patterns = S => {
  paperFrame('The same map, two rules for number patterns','同一张图，两种数值规则');
  graph(1,true);
  txt('Subtract neighbors',1300,300,{size:31,fam:F.disp,c:C.cyan});
  txt('L = D − A',1300,355,{size:41,fam:F.math});
  txt('Lx = 1x',1300,410,{size:41,fam:F.math,a:at(S,1,0.5)});
  txt('Add neighbors',1300,515,{size:31,fam:F.disp,c:C.mag});
  txt('Q = D + A',1300,570,{size:41,fam:F.math});
  txt('Qx = 3x',1300,625,{size:41,fam:F.math,a:at(S,1,0.5)});
  txt('Multiplicity counts independent patterns with the same factor.',250,815,{size:29,fam:F.disp,c:C.dim,a:at(S,2,0.5)});
};

SCENES.recurrence = S => {
  paperFrame('Symmetry turns the graph into a recurrence','利用对称性，把图上的问题变成递推');
  txt('Unchanged by swapping routes',170,315,{size:31,fam:F.disp,c:C.cyan});
  txt('Reverses sign after swapping',1050,315,{size:31,fam:F.disp,c:C.mag});
  txt('next = t × current − previous',W/2,420,{size:44,fam:F.math,align:'center',a:at(S,1,0.5)});
  const sequence=['A','s','s − A','−A','−s','A − s'];
  sequence.forEach((s,i)=>{
    const x=220+i*290,a=clamp(at(S,1,2.4)*6-i);
    txt(s,x,555,{size:42,fam:F.math,align:'center',a});
    txt(String(i+1),x,610,{size:24,fam:F.mono,align:'center',c:C.dim,a});
    if(i<5) arrow(x+95,540,x+195,540,C.dim,a,2);
  });
  txt('At t = 1, six steps return to the starting pair.',W/2,700,{size:32,fam:F.disp,align:'center',c:C.now,a:at(S,1,0.8)});
  txt('Endpoint conditions decide which patterns can meet.',W/2,795,{size:32,fam:F.disp,align:'center',a:at(S,2,0.5)});
};

SCENES.family = S => {
  paperFrame('The separation repeats forever','这种差异可以无穷地重复下去');
  txt('Long route: r = 6k + 4,  k ≥ 1',W/2,300,{size:48,fam:F.math,align:'center'});
  const columns=[{x:410,label:'Landmarks',zh:'最少地标数',value:'2'},
    {x:960,label:'L: maximum multiplicity',zh:'L 的最大重数',value:'2'},
    {x:1510,label:'Q: maximum multiplicity',zh:'Q 的最大重数',value:'1'}];
  columns.forEach((c,i)=>{
    const a=i===0?1:at(S,1,0.5);
    txt(c.label,c.x,420,{size:29,fam:F.disp,align:'center',a});
    txt(c.zh,c.x,470,{size:26,fam:F.zh,align:'center',c:C.dim,a});
    txt(c.value,c.x,610,{size:110,fam:F.math,align:'center',c:C.argued,a});
  });
  txt('r = 10, 16, 22, …     vertices = 15, 21, 27, …',W/2,720,{size:35,fam:F.math,align:'center',a:at(S,2,0.5)});
  txt('Connected and twin-free. Written proof: manuscript Theorem 1.',W/2,810,{size:28,fam:F.disp,align:'center',c:C.dim,a:at(S,2,0.5)});
};

SCENES.credit = S => {
  paperFrame('A new answer built on earlier mathematics','新的答案，建立在前人的数学之上');
  const lines=[
    ['Original question','Alfuraidan · Khan · Sauras-Altuzarra (2026)'],
    ['Metric classification','Knor · Sedlar · Škrekovski (2022)'],
    ['Spectral extension','Haobo Ma · Wenlin Zhang']
  ];
  lines.forEach(([label,name],i)=>{
    txt(label,180,330+i*135,{size:25,fam:F.disp,c:C.dim});
    txt(name,180,380+i*135,{size:37,fam:F.disp});
  });
  txt('Read the story. Explore the proof. Contribute a formalization.',W/2,810,{size:32,fam:F.disp,align:'center',c:C.now,a:at(S,2,0.5)});
};

FILM.poster = () => {
  paperFrame('Two landmarks. Two spectral rules.','两个地标，两种谱论规则');
  graph(1);
  txt('2 = maximum L multiplicity',1270,420,{size:31,fam:F.disp,c:C.cyan});
  txt('2 ≠ maximum Q multiplicity',1270,485,{size:31,fam:F.disp,c:C.mag});
  txt('A twin-free infinite family',1270,600,{size:31,fam:F.disp});
  txt('Haobo Ma · Wenlin Zhang',W/2,815,{size:32,fam:F.disp,align:'center',c:C.dim});
};
