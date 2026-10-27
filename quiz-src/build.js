const fs = require('fs');
const path = require('path');
const dir = __dirname;
const out = path.join(dir, '..', 'ITDS211-Midterm-Quiz.html');
const read = f => JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));

// ข้อเดิมเลข 1-90 ต่อเนื่องจาก part1-3.json ส่วนข้อใหม่อ้างด้วย id
const old = [null, ...read('part1.json'), ...read('part2.json'), ...read('part3.json')];
const fresh = {};
for (const q of [...read('new0406.json'), ...read('new0708.json')]) fresh[q.id] = q;

// แต่ละชุด 30 ข้อ เรียงตามบท: Ch01 3, Ch02 3, Ch03 6, Ch04 6, Ch05 3, Ch06 3, Ch07 3, Ch08 3
const SETS = [
  [1, 9, 12,   16, 24, 26,   35, 42, 37, 52, 56, 59,   62, 64, 66, 72, 'na', 'nc',   75, 78, 79,   83, 85, 87,   'n7a', 'n7b', 'n7c',   'n8a', 'n8b', 'n8c'],
  [3, 5, 13,   18, 22, 28,   34, 43, 39, 53, 58, 50,   61, 63, 67, 73, 69, 'nb',   76, 80, 81,   84, 88, 89,   'n7d', 'n7e', 'n7f',   'n8d', 'n8e', 'n8f'],
  [4, 14, 2,   20, 23, 29,   36, 44, 40, 60, 54, 57,   65, 68, 70, 71, 74, 'nd',   77, 'ne', 82,   86, 90, 'nf',   'n7g', 'n7h', 'n7i',   'n8g', 'n8h', 'n8i']
];

const data = [];
const used = new Set();
SETS.forEach((set, si) => {
  if (set.length !== 30) throw new Error(`set ${si + 1} has ${set.length}`);
  set.forEach((ref, i) => {
    if (used.has(ref)) throw new Error('duplicate ' + ref);
    used.add(ref);
    const q = typeof ref === 'number' ? old[ref] : fresh[ref];
    if (!q) throw new Error('missing ' + ref);
    data.push({ id: `s${si + 1}-${i + 1}`, part: si + 1, ...q, id: `s${si + 1}-${i + 1}` });
  });
});
for (const q of data) {
  if (q.c.length !== 4 || q.a < 0 || q.a > 3 || !q.e || !q.d || new Set(q.c).size !== 4) throw new Error('bad ' + q.id);
}
const tally = {};
for (const q of data) tally[q.ch] = (tally[q.ch] || 0) + 1;
console.log(JSON.stringify(tally));

const json = JSON.stringify(data).replace(/</g, '\\u003c');
const tpl = fs.readFileSync(path.join(dir, 'template.html'), 'utf8');
if (!tpl.includes('/*__DATA__*/[]')) throw new Error('placeholder missing');
fs.writeFileSync(out, tpl.replace('/*__DATA__*/[]', () => json));
console.log('wrote', out, fs.statSync(out).size, 'bytes');
