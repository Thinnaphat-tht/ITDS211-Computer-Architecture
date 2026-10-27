"""สร้าง ITDS211-Tutoring-Summary.html จาก clip1-5.py + สไลด์ PDF
รันด้วย Python ที่มี pymupdf:  python build.py
"""
import base64, html, importlib.util, json, os, re, sys
import fitz

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
OUT = os.path.join(ROOT, "ITDS211-Tutoring-Summary.html")


def load(i):
    spec = importlib.util.spec_from_file_location(f"clip{i}", os.path.join(SRC, f"clip{i}.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.CLIP


CLIPS = [load(i) for i in range(1, 6)]

# ---- ข้อสอบ 6 ชุด (quiz1-6.py) + ตัวตรวจ ----
sys.path.insert(0, SRC)


def load_set(i):
    spec = importlib.util.spec_from_file_location(f"quiz{i}", os.path.join(SRC, f"quiz{i}.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SET


QSETS = [load_set(i) for i in range(1, 7)]
SEC_IDS = {f'{c["id"]}-{i}' for c in CLIPS for i in range(1, len(c["sections"]) + 1)}
_seen = set()
for _si, _set in enumerate(QSETS, 1):
    assert len(_set) == 30, f"ชุด {_si} มี {len(_set)} ข้อ ต้องเป็น 30"
    for _qi, _q in enumerate(_set, 1):
        _w = f"ชุด {_si} ข้อ {_qi}"
        assert len(_q["c"]) == 4 and len(set(_q["c"])) == 4, _w + ": ตัวเลือกต้อง 4 ข้อไม่ซ้ำ"
        assert 0 <= _q["a"] < 4, _w + ": ดัชนีคำตอบผิด"
        assert _q["q"].strip() and _q["e"].strip() and _q["d"].strip(), _w + ": ขาดโจทย์/คำอธิบาย"
        assert f'v{_q["clip"]}-{_q["sec"]}' in SEC_IDS, _w + ": ลิงก์หัวข้อไม่มีจริง"
        assert _q["lv"] in (1, 2, 3), _w + ": ระดับผิด"
        assert _q["q"] not in _seen, _w + ": โจทย์ซ้ำ"
        _seen.add(_q["q"])
_cnt = [[sum(1 for q in s if q["clip"] == k) for k in range(1, 6)] for s in QSETS]
_lv = [[sum(1 for q in s if q["lv"] == k) for k in (1, 2, 3)] for s in QSETS]
print("quiz: คลิป1-5 ต่อชุด", _cnt, "| ระดับ 1/2/3 ต่อชุด", _lv)
QUIZ = [
    [
        {"id": f"s{si}-{qi}", "clip": q["clip"], "ref": f'v{q["clip"]}-{q["sec"]}', "lv": q["lv"], "q": q["q"], "c": q["c"], "a": q["a"], "e": q["e"], "d": q["d"]}
        for qi, q in enumerate(s, 1)
    ]
    for si, s in enumerate(QSETS, 1)
]

# ---- รูปสไลด์ (ฝัง base64 ครั้งเดียวต่อหน้า) ----
docs, imgs = {}, {}


def pdf_path(ch):
    name = "Chapter03_RiscV" if ch == "Chapter03" else ch
    return os.path.join(ROOT, f"itds-211_comp_arch_{name}.pdf")


def slide_key(ch, p):
    key = f"{ch[-2:]}-{p}"
    if key not in imgs:
        d = docs.setdefault(ch, fitz.open(pdf_path(ch)))
        page = d[p - 1]
        z = 900 / page.rect.width
        pix = page.get_pixmap(matrix=fitz.Matrix(z, z), alpha=False)
        imgs[key] = "data:image/jpeg;base64," + base64.b64encode(pix.tobytes("jpg", jpg_quality=72)).decode()
    return key


def figs(slides):
    if not slides:
        return ""
    out = ['<div class="figs n%d">' % min(len(slides), 3)]
    for ch, p in slides:
        k = slide_key(ch, p)
        out.append(
            f'<figure><img data-k="{k}" alt="สไลด์ Ch{ch[-2:]} หน้า {p}" loading="lazy">'
            f"<figcaption>สไลด์ Ch{ch[-2:]} · หน้า {p}</figcaption></figure>"
        )
    out.append("</div>")
    return "".join(out)


# ---- ประกอบเนื้อหา ----
nav, body = [], []
for ci, c in enumerate(CLIPS, 1):
    sub = []
    secs = []
    for si, s in enumerate(c["sections"], 1):
        sid = f'{c["id"]}-{si}'
        sub.append(f'<a class="sub" href="#{sid}"><span class="t">{html.escape(s["time"])}</span>{html.escape(s["title"])}</a>')
        chh = f'<h2 class="chh">{html.escape(s["ch"])}</h2>' if s.get("ch") else ""
        secs.append(
            f'{chh}<article class="sec" id="{sid}"><header><span class="chip">{html.escape(s["time"])}</span>'
            f'<h3>{html.escape(s["title"])}</h3></header>{figs(s["slides"])}<div class="txt">{s["body"]}</div></article>'
        )
    nav.append(
        f'<a class="nav" href="#{c["id"]}"><span class="n">{ci}</span>{html.escape(c["title"])}</a>'
        f'<div class="subs">{"".join(sub)}</div>'
    )
    body.append(
        f'<section class="clip" id="{c["id"]}"><div class="clip-head"><div class="clip-no">คลิปที่ {ci} · {html.escape(c["file"])} · ความยาว {html.escape(c["dur"])}</div>'
        f'<h1>{html.escape(c["title"])}</h1><p class="scope">{html.escape(c["scope"])}</p></div>'
        f'<div class="intro">{c["intro"]}</div>{"".join(secs)}</section>'
    )

QUIZ_JSON = json.dumps(QUIZ, ensure_ascii=False).replace("</", "<\\/")
QUIZ_NAV = (
    '<a class="nav" href="#quiz"><span class="n">✎</span>ข้อสอบ 6 ชุด (180 ข้อ)</a><div class="subs">'
    + "".join(f'<a class="sub" href="#quiz-{i}"><span class="t">ชุด {i}</span>30 ข้อ · ผสมครบ 5 คลิป</a>' for i in range(1, 7))
    + "</div>"
)
QUIZ_BODY = """<section class="clip" id="quiz"><div class="clip-head"><div class="clip-no">ทดสอบความเข้าใจ · 6 ชุด × 30 ข้อ</div>
<h1>ข้อสอบจากเนื้อหาคลาสติว</h1>
<p class="scope">ออกจากเนื้อหาในไฟล์นี้ (สิ่งที่อาจารย์พูด + ข้อเท็จจริงบนสไลด์ที่แสดง) ทุกชุดผสมครบทั้ง 5 คลิป ตอบแล้วเฉลยทันที มีคำอธิบายและลิงก์กลับไปอ่านหัวข้อต้นทาง ผลคะแนนถูกจำไว้ในเบราว์เซอร์ของคุณ</p></div>
<div class="box key nolabel"><ul><li>โจทย์ <b>Sign-Magnitude / 2's Complement</b> ผมแต่งจากหลักพื้นฐาน (ไฟล์สรุปไม่มีขั้นตอนคำนวณ) ตรวจคำตอบด้วยการคำนวณแล้ว แต่ควรเทียบกับสไลด์ Ch03 อีกครั้ง</li>
<li>ระดับของแต่ละข้อ: <b>ง่าย</b> (จำตรง ๆ) · <b>กลาง</b> (เข้าใจเหตุผล/คำนวณ) · <b>หลอก</b> (ตัวเลือกใกล้เคียง อ่านดี ๆ)</li></ul></div>
<div id="qsum"></div><div class="qsets" id="qsets"></div><div id="qview"></div></section>"""

cards = "".join(
    f'<a class="card" href="#{c["id"]}"><div class="no">คลิปที่ {i} · {html.escape(c["dur"])}</div>'
    f'<h4>{html.escape(c["title"])}</h4><p>{html.escape(c["scope"])}</p></a>'
    for i, c in enumerate(CLIPS, 1)
)
cards += (
    '<a class="card" href="#quiz"><div class="no">ข้อสอบ · 6 ชุด × 30 ข้อ</div><h4>ทดสอบความเข้าใจ</h4>'
    "<p>ทำข้อสอบจากเนื้อหาในไฟล์นี้ ตอบแล้วเฉลยทันที พร้อมลิงก์กลับไปอ่านทวน</p></a>"
)

HOME = """
<section class="clip home" id="top">
<div class="hero"><div class="clip-no">ติวก่อนสอบ Midterm · ITDS-211 Computer Architecture &amp; OS · 25 ต.ค. 2569</div>
<h1>สรุปสิ่งที่อาจารย์พูดในคลาสติว</h1>
<p>สรุปจากวิดีโอ 5 คลิป (รวมประมาณ 2 ชั่วโมง 22 นาที) เรียงตามลำดับที่อาจารย์สอน แต่ละหัวข้อมีรูปสไลด์ที่ตรงกันจากไฟล์ PDF ของวิชา</p></div>
<div class="cards">__CARDS__</div>

<h2>จุดที่อาจารย์พูดเกี่ยวกับข้อสอบ แยกเป็นหมวด (รวมจากทั้ง 5 คลิป)</h2>
<p class="note">กดที่ป้าย "คลิป n" เพื่อกระโดดไปหัวข้อต้นทาง · หมวด 1–4 เป็นสิ่งที่อาจารย์พูด หมวด 5–6 มีส่วนที่ผมสรุปเอง (ระบุไว้ในข้อ)</p>

<div class="box key nolabel"><h3>1) รูปแบบและกติกาการสอบ</h3><ul>
<li>ข้อสอบเป็น <b>multiple choice 60 ข้อ</b> (นักศึกษาถาม อาจารย์ตอบ "ใช่เลยครับ") __S4_17__</li>
<li>เอากระดาษเข้าห้องสอบได้ <b>2 แผ่น A4</b> · <b>ปริ้นต์ได้</b> ไม่ต้องเขียนมือก็ได้ __S5_9__</li>
<li><b>เปิดสไลด์ในห้องสอบไม่ได้</b> __S5_9__</li>
<li>อาจารย์จะ <b>"แกล้งสัก 2–3 ข้อ"</b> นอกนั้น <b>ทุกอย่างอยู่ในสไลด์ และอาจอยู่ใน assignment</b> __S1_intro__</li>
</ul></div>

<div class="box exam nolabel"><h3>2) เน้น — อาจารย์พูดชัดว่าจะออก / ให้จำ / ให้ดูดี ๆ</h3><ul>
<li><b>คำนวณ Sign-Magnitude และ 2's Complement</b>: <b>"จะมีข้อนี้แน่ๆ บอกไว้เลย"</b> ต้องทำให้ได้เต็ม (เหมือนใน assignment) __S1_16__</li>
<li><b>ขั้นตอนเมื่อเกิด Interrupt</b> (เซฟค่า → ดู Interrupt Vector หา ISR → ใส่ PC กระโดดไปทำ → restore แล้วกลับ): อาจารย์บอก <b>"จำไว้เลย"</b> __S1_14__</li>
<li><b>CPI และสูตร CPU time</b> (Instruction count × CPI × Cycle time): อาจารย์ย้ำให้ <b>"ดูดีๆ"</b> __S1_6__</li>
<li><b>Ch04: จำรูปพีระมิดหน่วยความจำ</b> และ <b>เน้นเรื่อง Cache</b> (hit/miss, direct-mapped, tag/index/valid bit, set-associative) __S2_4__</li>
<li><b>Ch06 Storage: ออกไม่เยอะ</b> แต่ตรงไปที่ <b>Hard disk</b> หลักการเขียน/อ่านและการทำงาน __S4_4__</li>
<li>ตอนปิดคลิป 4 หลังไล่ Ch05–08 จบ: <b>"ท้ายสุดน่าจะเป็นประมาณนี้ ที่อาจารย์จะออกในข้อสอบ"</b> __S4_16__</li>
<li>ปิดคลาสในคลิป 5: <b>"คำถามสไตล์ประมาณแบบเนี้ย ไปทบทวนเนาะ"</b> (โจทย์สั้น 15 ข้อ พร้อมคำตอบ อยู่ในคลิป 5) __S5_1__</li>
</ul></div>

<div class="box ex nolabel"><h3>3) ระดับพื้นฐาน / ไม่ยาก — อาจารย์บอกว่าง่าย</h3><ul>
<li><b>Ch01 องค์ประกอบคอมพิวเตอร์และ CPU:</b> "basic มากๆ" __S1_1__</li>
<li><b>Register PC / IR / Status:</b> "ไม่น่ามีประเด็น" __S1_3__</li>
<li><b>เปรียบเทียบ Performance (เท่าตัว):</b> "บัญญัติไตรยางศ์ง่ายๆ เป็นเรื่อง relative ธรรมดา" ให้อ่านโจทย์ดี ๆ ว่าเร็วกว่า = ใช้เวลาน้อยกว่า __S1_5__</li>
<li><b>Assembly:</b> เป็นช้อยส์ ต้องเข้าใจแค่ว่าคำสั่งทำอะไร (ADD, LOAD, STORE, ADDI, beq/bne/blt/bge, AND/OR/XOR, shift) ไม่ต้องเขียนโค้ด __S1_17__ __S2_2__</li>
<li><b>Procedure / software interrupt:</b> ส่วนที่เหลือของ Assembly "ไม่น่ามีอะไร" __S2_3__</li>
<li><b>Ch05 คำถามจาก assignment</b> (USB vs SCSI, Thunderbolt, InfiniBand ใช้กับอะไร): แนวทั่วไป "basic ไม่ยากมาก" __S4_3__</li>
</ul></div>

<div class="box warn nolabel"><h3>4) ไม่ออก / ไม่ต้องลงลึก</h3><ul>
<li><b>ส่วน self study เฉพาะ RISC-V</b> ที่อาจารย์ทิ้งไว้ให้อ่านเอง: <b>"ไม่ได้ออกข้อสอบ"</b> __S2_3__</li>
<li><b>ไม่เจาะจงตระกูล</b> RISC-V / MIPS / ARM: เป็นความรู้ทั่วไป ไม่ต้องท่องคำสั่งเฉพาะตระกูล __S1_17__</li>
<li><b>ไม่ต้องเขียนโค้ด Assembly</b> (ข้อสอบเป็นช้อยส์) __S1_17__</li>
<li><b>MISD:</b> อาจารย์บอกว่า "ไม่มีเลยแล้ว" (เป็นข้อเท็จจริง ไม่ได้บอกว่าไม่ออกสอบ) __S4_13__</li>
</ul></div>

<div class="box plain nolabel"><h3>5) อาจารย์พูดถึง แต่ไม่ได้บอกว่าออกหรือไม่ออก</h3><ul>
<li><b>Write-through / Write-back / Write-allocation:</b> อาจารย์เล่าเป็นประวัติว่างานวิจัยลดลงเพราะ memory เร็วขึ้น แต่ใน<b>คลิป 5 อาจารย์ก็ถามชื่อทั้งสามแบบ</b> (ควรรู้นิยาม) __S2_11__ __S5_6__</li>
<li><b>Ch03 (Data Representation / Floating point):</b> อาจารย์ถามเรื่อง IEEE 754 exponent (single 8 บิต / double 11 บิต) ในคลิป 5 พอนักศึกษาถามว่า "ถามบท 3 เยอะ แปลว่าออกเยอะไหม" อาจารย์ตอบหยอกว่า <b>"จำข้อสอบไม่ได้แล้ว"</b> __S5_4__</li>
<li><b>Ch07 Pipeline และ Ch08 Parallel/GPU:</b> อาจารย์ไล่สอนในคลาสติว แต่ไม่ได้ระบุเป็นหัวข้อเน้นเอง (ผมไม่ทราบว่าอยู่ในขอบเขตสอบหรือไม่ ให้เช็คกับประกาศ/อาจารย์) __S4_8__</li>
<li><b>Hazard 3 แบบ, Flynn's taxonomy, RAID:</b> อธิบายละเอียดในคลิป 4 ไม่มีคำบอกระดับความสำคัญ __S4_9__ __S4_13__ __S4_6__</li>
</ul></div>

<div class="box nolabel"><h3>6) หัวข้อในสไลด์ที่ "ไม่พบ" ในซับของคลิป (ผมสรุปเอง)</h3>
<p style="margin:.3em 0">เท่าที่ซับถอดได้ ไม่พบคำพูดถึง: <b>Virtual memory / Page table / TLB</b>, <b>Hamming code (SEC/DED)</b>, <b>Cache coherence</b>, <b>Dependability (MTTF/MTTR)</b>, <b>MARIE</b> (Ch02 หน้า 17–27) และรายละเอียดเชิงลึกของ <b>Floating point</b></p>
<p class="note" style="margin:.3em 0">"ไม่พบในซับ" <b>ไม่เท่ากับ "ไม่ออก"</b> ซับขาดบางช่วง (คลิป 2 ช่วง 25:00–26:51 อาจารย์เปิดสไลด์ Dependability Measures อยู่ แต่ไม่มีเสียงที่ถอดได้) ถ้าห่วงหัวข้อไหนเป็นพิเศษ ให้ถามอาจารย์หรือยึดตามประกาศ</p></div>
<div class="box warn"><b>ข้อจำกัดของสรุปนี้:</b>
<ul>
<li>ทำจากซับที่ <b>Gemini ถอดเสียง</b> ไม่ใช่การฟังเสียงโดยตรง อาจมีคำผิด ผมเทียบศัพท์และตัวเลขกับสไลด์ในหลายจุด</li>
<li><b>คลิป 2 ไม่มีซับ</b> ช่วง 25:00–26:51 · <b>คลิป 3</b> ซับถึง 10:58 · <b>คลิป 4</b> เวลาในซับเพี้ยนหลายนาที ผมใช้เวลาจากสไลด์ที่เห็นในวิดีโอแทน</li>
<li>ข้อความที่เป็น "คำพูดอาจารย์" เขียนตามที่ซับถอดได้ ส่วนที่ผมเสริมจากสไลด์ติดป้ายบอกไว้ในหมายเหตุของหัวข้อนั้น</li>
</ul></div>
</section>
""".replace("__CARDS__", cards)
# ป้ายลิงก์ __S{คลิป}_{หัวข้อ}__ -> ลิงก์ไปหัวข้อต้นทาง
HOME = re.sub(
    r"__S(\d)_(\w+)__",
    lambda m: f'<a class="src" href="#v{m.group(1)}{"" if m.group(2) == "intro" else "-" + m.group(2)}">คลิป {m.group(1)}</a>',
    HOME,
)

CSS = r"""
:root{--bg:#f4f7fc;--surface:#fff;--surface2:#e8eef8;--ink:#1b2433;--muted:#5a6b82;--line:#d3dcec;--accent:#2563eb;--accent-soft:#dbe8ff;
--key:#e3edff;--key-b:#2563eb;--formula:#fff4d6;--formula-b:#c88a00;--ex:#eef3f9;--ex-b:#4a6c91;--warn:#fde8e4;--warn-b:#c2410c;--exam:#f1ecfa;--exam-b:#7a5aa6;--chip:#2563eb}
:root[data-theme="dark"]{--bg:#0f1623;--surface:#161f30;--surface2:#1e2a40;--ink:#e6ecf7;--muted:#9fb1cc;--line:#2b3a55;--accent:#6ea8ff;--accent-soft:#1b2f55;
--key:#14284a;--key-b:#6ea8ff;--formula:#33290e;--formula-b:#e0a82e;--ex:#1b2733;--ex-b:#7ba3cf;--warn:#3a1f19;--warn-b:#f08a5d;--exam:#2a2238;--exam-b:#b79be0;--chip:#6ea8ff}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0f1623;--surface:#161f30;--surface2:#1e2a40;--ink:#e6ecf7;--muted:#9fb1cc;--line:#2b3a55;--accent:#6ea8ff;--accent-soft:#1b2f55;
--key:#14284a;--key-b:#6ea8ff;--formula:#33290e;--formula-b:#e0a82e;--ex:#1b2733;--ex-b:#7ba3cf;--warn:#3a1f19;--warn-b:#f08a5d;--exam:#2a2238;--exam-b:#b79be0;--chip:#6ea8ff}}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:72px}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"IBM Plex Sans Thai",system-ui,sans-serif;font-size:17px;line-height:1.75}
code{font-family:"JetBrains Mono",ui-monospace,Consolas,monospace;background:var(--surface2);padding:.08em .38em;border-radius:5px;font-size:.88em;word-break:break-word}
.topbar{position:sticky;top:0;z-index:30;display:flex;align-items:center;gap:10px;padding:10px 16px;background:var(--surface);border-bottom:1px solid var(--line)}
.topbar .title{font-weight:700;font-size:1rem;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.btn{font:inherit;cursor:pointer;border:1px solid var(--line);background:var(--surface2);color:var(--ink);padding:7px 12px;border-radius:9px;font-size:.9rem}
.btn:hover{border-color:var(--accent)}.btn:focus-visible,a:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
#menu{display:none}
.shell{display:grid;grid-template-columns:310px minmax(0,1fr);min-height:calc(100vh - 56px)}
.side{position:sticky;top:56px;align-self:start;height:calc(100vh - 56px);overflow-y:auto;padding:14px;border-right:1px solid var(--line);background:var(--surface)}
.side a{display:block;color:var(--ink);text-decoration:none;border-radius:9px;line-height:1.35}
.side a.nav{padding:9px 11px;font-weight:600;font-size:.95rem;margin-top:8px}
.side a.nav .n{display:inline-block;min-width:1.7em;color:var(--accent);font-family:"JetBrains Mono",monospace;font-size:.85rem}
.side a.sub{padding:5px 11px 5px 30px;font-size:.84rem;color:var(--muted)}
.side a.sub .t{font-family:"JetBrains Mono",monospace;font-size:.72rem;margin-right:7px;color:var(--accent)}
.side a:hover{background:var(--surface2)}.side a.on{background:var(--accent-soft);color:var(--ink)}
main{padding:28px clamp(16px,4vw,56px) 80px;max-width:1000px;width:100%}
.clip{margin-bottom:56px}
.hero h1,.clip-head h1{font-size:clamp(1.6rem,3.8vw,2.3rem);line-height:1.3;margin:.2em 0 .3em}
.hero p,.scope{color:var(--muted)}.scope{margin:.2em 0 0}
.clip-no{font-family:"JetBrains Mono",monospace;color:var(--accent);font-weight:600;font-size:.82rem;letter-spacing:.04em}
.clip-head{padding:6px 0 14px;border-bottom:2px solid var(--line);margin-bottom:16px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px;margin:24px 0}
.card{display:block;text-decoration:none;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:14px 16px;transition:transform .15s,border-color .15s}
.card:hover{transform:translateY(-2px);border-color:var(--accent)}.card .no{font-family:"JetBrains Mono",monospace;font-size:.76rem;color:var(--accent);font-weight:600}
.card h4{margin:.25em 0 .3em;font-size:1rem;line-height:1.35}.card p{margin:0;color:var(--muted);font-size:.84rem;line-height:1.5}
h2{font-size:1.3rem;margin:1.6em 0 .6em;padding-bottom:.25em;border-bottom:1px solid var(--line)}
h2.chh{color:var(--accent);font-size:1.15rem;margin-top:2em}
.sec{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:14px 18px 8px;margin:14px 0}
.sec header{display:flex;gap:12px;align-items:baseline;flex-wrap:wrap}
.sec h3{margin:0;font-size:1.1rem;line-height:1.4}
.chip{font-family:"JetBrains Mono",monospace;font-size:.78rem;background:var(--accent-soft);color:var(--ink);border:1px solid var(--chip);border-radius:999px;padding:1px 10px;white-space:nowrap}
.txt p{margin:.6em 0}.txt ul,.txt ol{padding-left:1.4em;margin:.5em 0}.txt li{margin:.3em 0}
.note{color:var(--muted);font-size:.9rem}.src{font-size:.72rem;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:0 7px;margin-left:4px;white-space:nowrap}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:.93rem;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:8px 11px;vertical-align:top;text-align:left}th{background:var(--surface2)}
.box{border-left:5px solid var(--b,var(--accent));background:var(--bg-b,var(--key));padding:12px 16px;border-radius:0 12px 12px 0;margin:14px 0}
.box>:first-child{margin-top:0}.box>:last-child{margin-bottom:0}.box ul{margin:.3em 0}
.box.key{--bg-b:var(--key);--b:var(--key-b)}.box.formula{--bg-b:var(--formula);--b:var(--formula-b)}
.box.ex{--bg-b:var(--ex);--b:var(--ex-b)}.box.warn{--bg-b:var(--warn);--b:var(--warn-b)}.box.exam{--bg-b:var(--exam);--b:var(--exam-b)}
.box.plain{--bg-b:var(--surface2);--b:var(--muted)}.box h3{margin:0 0 .4em;font-size:1.02rem;color:var(--ink)}
.box.nolabel::before{display:none!important}.src a,a.src{text-decoration:none;color:var(--accent)}a.src{font-size:.72rem;border:1px solid var(--line);border-radius:999px;padding:0 7px;margin-left:4px;white-space:nowrap}a.src:hover{border-color:var(--accent);background:var(--accent-soft)}
.box.formula::before,.box.ex::before,.box.exam::before,.box.warn::before{display:block;font-size:.72rem;letter-spacing:.1em;font-weight:700}
.box.formula::before{content:"สูตร";color:var(--formula-b)}.box.ex::before{content:"ตัวอย่าง";color:var(--ex-b)}
.box.exam::before{content:"เน้นสอบ / อาจารย์พูดถึงข้อสอบ";color:var(--exam-b)}.box.warn::before{content:"ระวัง";color:var(--warn-b)}
.figs{display:grid;gap:10px;margin:10px 0;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.figs.n1{grid-template-columns:minmax(0,640px)}
figure{margin:0}figure img{width:100%;height:auto;display:block;border:1px solid var(--line);border-radius:10px;background:#fff;cursor:zoom-in}
figcaption{font-size:.76rem;color:var(--muted);margin-top:3px}
#lb{position:fixed;inset:0;background:rgba(0,0,0,.85);display:none;align-items:center;justify-content:center;z-index:99;cursor:zoom-out;padding:16px}
#lb.on{display:flex}#lb img{max-width:100%;max-height:100%;border-radius:8px;background:#fff}
.rail{position:fixed;right:0;top:56px;bottom:0;width:min(92vw,340px);z-index:35;overflow-y:auto;padding:14px 16px 20px;background:var(--surface);border-left:1px solid var(--line);font-size:.88rem;transform:translateX(102%);transition:transform .2s;visibility:hidden}
.rail.open{transform:none;visibility:visible;box-shadow:0 0 24px rgba(0,0,0,.18)}
@media (min-width:1500px){body.rail-on .shell{padding-right:340px}.rail.open{box-shadow:none}}
.rail .rh{display:flex;justify-content:space-between;align-items:flex-start;gap:8px}
.rail h3{margin:0 0 4px;font-size:1rem}.rail .sub{color:var(--muted);font-size:.78rem;margin:0 0 10px}
.rail .x{font:inherit;cursor:pointer;border:1px solid var(--line);background:var(--surface2);color:var(--ink);border-radius:8px;padding:2px 9px;line-height:1.4}.rail .x:hover{border-color:var(--accent)}
.rail h4{margin:14px 0 6px;font-size:.84rem;color:var(--muted)}
.rail ol{list-style:none;margin:0;padding:0}.rail li{margin:0 0 9px}
.rail .row{display:flex;justify-content:space-between;gap:8px}.rail .row b{font-weight:600}
.rail .row span{font-family:"JetBrains Mono",monospace;font-size:.76rem;color:var(--accent);white-space:nowrap}
.rail .bar{height:6px;border-radius:3px;background:var(--surface2);margin-top:3px;overflow:hidden}.rail .bar i{display:block;height:100%;background:var(--accent);border-radius:3px}
.rail .note{color:var(--muted);font-size:.74rem;line-height:1.5;margin:12px 0 0}
@media (max-width:860px){.shell{grid-template-columns:1fr}#menu{display:inline-block}
.side{position:fixed;left:0;top:56px;bottom:0;width:min(86vw,330px);height:auto;z-index:40;transform:translateX(-102%);transition:transform .2s}
.side.open{transform:none;box-shadow:0 0 30px rgba(0,0,0,.3)}body{font-size:16px}}
@media print{.topbar,.side,.rail{display:none}.shell{display:block}.sec{break-inside:avoid}}
.qsets{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;margin:16px 0}
.qcard{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:14px 16px}
.qcard.on{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent-soft)}
.qcard h4{margin:0 0 4px;font-size:1.05rem}.qcard .m{color:var(--muted);font-size:.85rem}
.bar{height:8px;background:var(--surface2);border-radius:99px;overflow:hidden;margin:8px 0}.bar i{display:block;height:100%;background:var(--accent)}
.bar i.w{background:var(--warn-b)}
.qbtn{display:inline-block;font:inherit;font-size:.9rem;cursor:pointer;text-decoration:none;color:var(--ink);background:var(--surface2);border:1px solid var(--line);padding:6px 12px;border-radius:9px}
.qbtn:hover{border-color:var(--accent)}.qbtn.pri{background:var(--accent);color:#fff;border-color:var(--accent)}.qbtn.armed{background:var(--warn);border-color:var(--warn-b)}
.qsumbox{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px 16px;margin:14px 0}
.qsumbox summary{cursor:pointer;font-weight:600}.qrow{display:flex;gap:10px;align-items:center;font-size:.88rem;margin:6px 0}.qrow b{min-width:7.5em}.qrow .bar{flex:1;margin:0}
.qtools{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:14px 0;position:sticky;top:56px;z-index:5;background:var(--bg);padding:8px 0}
.qtools .sp{flex:1}.qf.on{background:var(--accent-soft);border-color:var(--accent)}
.q{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:14px 18px;margin:14px 0}
.qh{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:4px}.qn{font-weight:700;color:var(--accent)}
.lvc{font-size:.72rem;border:1px solid var(--line);border-radius:999px;padding:0 8px;color:var(--muted)}
.qq{margin:.3em 0 .6em;font-weight:500}
.opts{display:grid;gap:8px}
.opt{display:flex;gap:10px;align-items:flex-start;text-align:left;font:inherit;cursor:pointer;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:9px 12px;line-height:1.5}
.opt:hover:not(:disabled){border-color:var(--accent)}.opt:disabled{cursor:default}
.opt .l{font-weight:700;color:var(--accent);min-width:1.4em}
.opt.ok{background:var(--key);border-color:var(--key-b);box-shadow:inset 4px 0 0 var(--key-b)}
.opt.bad{background:var(--warn);border-color:var(--warn-b);box-shadow:inset 4px 0 0 var(--warn-b)}
.fb{margin-top:10px;border-left:5px solid var(--key-b);background:var(--key);border-radius:0 10px 10px 0;padding:10px 14px}
.fb.bad{border-color:var(--warn-b);background:var(--warn)}.fb .res{font-weight:700;margin-bottom:4px}.fb .ex{margin:.3em 0}
.fb .more{margin-top:6px;padding-top:6px;border-top:1px dashed var(--line);display:none}.fb .more.on{display:block}.fb .acts{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
.qempty{color:var(--muted);padding:16px 0}
"""

JS = r"""
const IM=JSON.parse(document.getElementById('imgdata').textContent);
document.querySelectorAll('img[data-k]').forEach(i=>{i.src=IM[i.dataset.k]});
const root=document.documentElement,btn=document.getElementById('theme');
function cur(){return root.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}
function label(){btn.textContent=cur()==='dark'?'☀ โหมดสว่าง':'☾ โหมดมืด'}
try{const t=localStorage.getItem('tut-theme');if(t)root.dataset.theme=t}catch(e){}
label();
btn.onclick=()=>{const n=cur()==='dark'?'light':'dark';root.dataset.theme=n;try{localStorage.setItem('tut-theme',n)}catch(e){};label()};
(()=>{const r=document.getElementById('rail'),b=document.getElementById('railbtn');
function set(o,save){r.classList.toggle('open',o);document.body.classList.toggle('rail-on',o);b.setAttribute('aria-expanded',o);b.style.borderColor=o?'var(--accent)':'';if(save){try{localStorage.setItem('tut-rail',o?'1':'0')}catch(e){}}}
let st=null;try{st=localStorage.getItem('tut-rail')}catch(e){}
set(st===null?innerWidth>=1500:st==='1',false);
b.onclick=()=>set(!r.classList.contains('open'),true);document.getElementById('railx').onclick=()=>set(false,true)})();
const side=document.getElementById('side');
document.getElementById('menu').onclick=()=>side.classList.toggle('open');
side.addEventListener('click',e=>{if(e.target.closest('a'))side.classList.remove('open')});
const lb=document.getElementById('lb'),lbi=lb.querySelector('img');
document.addEventListener('click',e=>{const i=e.target.closest('figure img');if(i){lbi.src=i.src;lb.classList.add('on')}else if(e.target.closest('#lb'))lb.classList.remove('on')});
document.addEventListener('keydown',e=>{if(e.key==='Escape')lb.classList.remove('on')});
const links=[...document.querySelectorAll('.side a[href^="#"]')];const map=new Map(links.map(a=>[a.getAttribute('href').slice(1),a]));
const io=new IntersectionObserver(es=>{es.forEach(en=>{if(en.isIntersecting){links.forEach(l=>l.classList.remove('on'));const a=map.get(en.target.id);if(a){a.classList.add('on');a.scrollIntoView({block:'nearest'})}}})},{rootMargin:'-20% 0px -70% 0px'});
document.querySelectorAll('.sec,.clip').forEach(s=>s.id&&io.observe(s));

/* ===== ข้อสอบ ===== */
const QD=JSON.parse(document.getElementById('quizdata').textContent);
const QK='itds211-tutoring-quiz-v1';
let ST={perm:{},ans:{}};
try{const r=JSON.parse(localStorage.getItem(QK));if(r&&r.perm&&r.ans)ST=r}catch(e){}
function qsave(){try{localStorage.setItem(QK,JSON.stringify(ST))}catch(e){}}
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const LET=['ก','ข','ค','ง'],LV=['','ง่าย','กลาง','หลอก'];
function qperm(id){if(!ST.perm[id]){const p=[0,1,2,3];for(let i=3;i>0;i--){const j=Math.floor(Math.random()*(i+1));[p[i],p[j]]=[p[j],p[i]]}ST.perm[id]=p;qsave()}return ST.perm[id]}
function setStat(si){let d=0,c=0;QD[si].forEach(q=>{if(q.id in ST.ans){d++;if(ST.ans[q.id]===q.a)c++}});return{d,c,n:QD[si].length}}
let curSet=-1,filt='all',armed=null;
function pct(a,b){return b?Math.round(a*100/b):0}
function renderSummary(){
  let td=0,tc=0;const cl={};
  QD.forEach(s=>s.forEach(q=>{if(q.id in ST.ans){td++;const ok=ST.ans[q.id]===q.a;if(ok)tc++;const k=cl[q.clip]=cl[q.clip]||{d:0,c:0};k.d++;if(ok)k.c++}}));
  let rows='';for(let k=1;k<=5;k++){const x=cl[k]||{d:0,c:0};rows+=`<div class="qrow"><b>คลิปที่ ${k}</b><div class="bar"><i style="width:${pct(x.c,x.d)}%"></i></div><span>${x.c}/${x.d}</span></div>`}
  document.getElementById('qsum').innerHTML=`<div class="qsumbox"><div class="qrow"><b>ทั้งหมด</b><div class="bar"><i style="width:${pct(td,180)}%"></i></div><span>ทำแล้ว ${td}/180 · ถูก ${tc}</span></div>
  <details><summary>คะแนนแยกตามคลิป (เฉพาะข้อที่ทำแล้ว)</summary>${rows}</details>
  <div style="margin-top:8px"><button class="qbtn" id="rall">รีเซ็ตทั้งหมด</button></div></div>`;
  document.getElementById('rall').onclick=e=>confirmBtn(e.target,'all',()=>{ST={perm:{},ans:{}};qsave();renderAll()});
  document.getElementById('qsets').innerHTML=QD.map((s,i)=>{const t=setStat(i);return`<div class="qcard${i===curSet?' on':''}"><h4>ชุดที่ ${i+1}</h4><div class="m">ทำแล้ว ${t.d}/${t.n} · ถูก ${t.c}</div>
  <div class="bar"><i style="width:${pct(t.d,t.n)}%"></i></div><a class="qbtn pri" href="#quiz-${i+1}">${t.d?'ทำต่อ':'เริ่มทำ'}</a></div>`}).join('');
}
function confirmBtn(b,key,fn){if(armed===key){clearTimeout(b._t);armed=null;fn();return}armed=key;const o=b.textContent;b.textContent='กดอีกครั้งเพื่อยืนยัน';b.classList.add('armed');
  b._t=setTimeout(()=>{armed=null;b.textContent=o;b.classList.remove('armed')},3000)}
function cardHTML(q,n){
  const p=qperm(q.id),ans=ST.ans[q.id],done=q.id in ST.ans;
  const opts=p.map((oi,pos)=>{let cls='';if(done){if(oi===q.a)cls=' ok';else if(oi===ans)cls=' bad'}
    return`<button class="opt${cls}" data-oi="${oi}"${done?' disabled':''}><span class="l">${LET[pos]}</span><span>${esc(q.c[oi])}${done&&oi===q.a?' ✓':''}${done&&oi===ans&&oi!==q.a?' ✗':''}</span></button>`}).join('');
  let fb='';if(done){const ok=ans===q.a;fb=`<div class="fb${ok?'':' bad'}"><div class="res">${ok?'✓ ถูกต้อง':'✗ ยังไม่ถูก — เฉลย: ข้อ '+LET[p.indexOf(q.a)]}</div><div class="ex">${esc(q.e)}</div>
  <div class="more">${esc(q.d)}</div><div class="acts"><button class="qbtn more-b">ไม่เข้าใจ? อธิบายเพิ่ม</button><a class="qbtn" href="#${q.ref}">ดูหัวข้อที่เกี่ยวข้อง →</a></div></div>`}
  return`<article class="q" id="q-${q.id}" data-id="${q.id}"><div class="qh"><span class="qn">ข้อ ${n}</span><span class="chip">คลิป ${q.clip}</span><span class="lvc">${LV[q.lv]}</span></div>
  <p class="qq">${esc(q.q)}</p><div class="opts">${opts}</div>${fb}</article>`}
function renderSet(){
  const v=document.getElementById('qview');
  if(curSet<0){v.innerHTML='';return}
  const t=setStat(curSet);
  const list=QD[curSet].map((q,i)=>({q,n:i+1})).filter(x=>filt==='all'||(filt==='todo'&&!(x.q.id in ST.ans))||(filt==='wrong'&&(x.q.id in ST.ans)&&ST.ans[x.q.id]!==x.q.a));
  v.innerHTML=`<h2 id="qtop">ชุดที่ ${curSet+1}</h2><div class="qtools"><a class="qbtn" href="#quiz">← ทุกชุด</a>
  <button class="qbtn qf${filt==='all'?' on':''}" data-f="all">ทั้งหมด</button><button class="qbtn qf${filt==='todo'?' on':''}" data-f="todo">ยังไม่ทำ</button><button class="qbtn qf${filt==='wrong'?' on':''}" data-f="wrong">ตอบผิด</button>
  <span class="sp"></span><span class="m">ทำแล้ว ${t.d}/${t.n} · ถูก ${t.c}</span><button class="qbtn" id="rset">รีเซ็ตชุดนี้</button></div>
  ${list.length?list.map(x=>cardHTML(x.q,x.n)).join(''):'<div class="qempty">ไม่มีข้อที่ตรงกับตัวกรองนี้</div>'}
  <div class="qtools" style="position:static"><a class="qbtn" href="#quiz">← ทุกชุด</a>${curSet<5?`<a class="qbtn pri" href="#quiz-${curSet+2}">ชุดถัดไป →</a>`:''}</div>`;
  v.querySelectorAll('.qf').forEach(b=>b.onclick=()=>{filt=b.dataset.f;renderSet()});
  document.getElementById('rset').onclick=e=>confirmBtn(e.target,'set',()=>{QD[curSet].forEach(q=>{delete ST.ans[q.id];delete ST.perm[q.id]});qsave();renderAll()});
}
function renderAll(){renderSummary();renderSet()}
document.getElementById('qview').addEventListener('click',e=>{
  const o=e.target.closest('.opt');
  if(o&&!o.disabled){const id=o.closest('.q').dataset.id;ST.ans[id]=+o.dataset.oi;qsave();
    const si=+id.split('-')[0].slice(1)-1,q=QD[si].find(x=>x.id===id),n=QD[si].indexOf(q)+1;
    o.closest('.q').outerHTML=cardHTML(q,n);renderSummary();
    const t=setStat(curSet),m=document.querySelector('.qtools .m');if(m)m.textContent=`ทำแล้ว ${t.d}/${t.n} · ถูก ${t.c}`;return}
  const mb=e.target.closest('.more-b');if(mb){const m=mb.closest('.fb').querySelector('.more');m.classList.toggle('on');mb.textContent=m.classList.contains('on')?'ซ่อนคำอธิบาย':'ไม่เข้าใจ? อธิบายเพิ่ม'}
});
function route(){
  const m=/^#quiz-(\d)$/.exec(location.hash);
  if(m){const s=+m[1]-1;if(s>=0&&s<6){if(curSet!==s)filt='all';curSet=s;renderAll();document.getElementById('qtop').scrollIntoView();return}}
  if(location.hash==='#quiz'){curSet=-1;renderAll()}
}
window.addEventListener('hashchange',route);
renderAll();if(location.hash.startsWith('#quiz'))route();
"""


_T=[("Memory Hierarchy + Cache","29:40",29.67,"Cache ~20:45 · Pyramid/SRAM/DRAM/RAM-ROM ~8:55"),
("Parallel: Flynn · SIMD · Vector · GPU","15:00",14.97,""),
("Pipeline: 3 Hazard · Forwarding","14:20",14.32,""),
("I/O (ไม่รวม Interrupt)","14:15",14.25,"I/O Module · Programmed/Interrupt/DMA"),
("Data Rep + Assembly + IEEE 754","13:20",13.3,"Sign-Mag · 2's Comp · Endian · R/I-format"),
("Bus: Arbitration · Daisy Chain","12:45",12.73,""),
("Interrupt: Nested · Device ID","9:35",9.6,""),
("Storage: HDD · RAID · SSD · CD/DVD","8:05",8.07,""),
("Ch2 อื่น ๆ: Von Neumann · Register · Instruction flow","6:30",6.5,""),
("Ch1: CPU · Performance · CPI","5:50",5.87,"")]
_S=[("Daisy Chain และ Bus Arbitrator (คลิป 5)","5:09"),
("Direct-Mapped: Tag, Index, Valid bit (คลิป 2)","4:22"),
("สรุป Pipeline: 3 hazard + Pipeline Registers (คลิป 4)","4:20"),
("SISD = 1 คำสั่ง 1 ข้อมูล (คลิป 5)","4:18"),
("Data Hazard และวิธีแก้ (คลิป 4)","3:40"),
("Flynn's Taxonomy (คลิป 4)","3:40")]
RANK = '<aside class="rail" id="rail"><div class="rh"><h3>อาจารย์พูดเรื่องไหนนานสุด</h3><button class="x" id="railx" aria-label="ปิด">✕</button></div><p class="sub">วัดจากเวลาเริ่มหัวข้อในคลิปทั้ง 5 · รวม ~140 นาที</p><ol>' + "".join(
    f'<li><div class="row"><b>{i}. {t}</b><span>{m}</span></div><div class="bar"><i style="width:{w/29.67*100:.0f}%"></i></div>'
    + (f'<div class="note" style="margin:3px 0 0">{n}</div>' if n else '') + '</li>'
    for i, (t, m, w, n) in enumerate(_T, 1)) + '</ol><h4>หัวข้อย่อยที่ยาวสุด</h4><ol>' + "".join(
    f'<li><div class="row"><b>{t}</b><span>{m}</span></div></li>' for t, m in _S) + '</ol>'     '<p class="note">เวลา ≠ จำนวนคำ · เวลาคลิป 4 เป็นค่าประมาณ · ไม่นับ Q&amp;A/ปิดคลาส (~11 นาที) · คลิป 5 เป็นการทบทวน หัวข้อที่พูดซ้ำถูกรวมเข้าด้วยกัน</p></aside>'

page = f"""<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>สรุปคลาสติว ITDS-211</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="topbar"><button class="btn" id="menu" aria-label="เมนู">☰</button><div class="title">สรุปคลาสติว ITDS-211 · Midterm</div><button class="btn" id="railbtn" aria-expanded="false">อันดับเวลา</button><button class="btn" id="theme">☾ โหมดมืด</button></div>
<div class="shell">
<nav class="side" id="side"><a class="nav" href="#top"><span class="n">★</span>ภาพรวมและจุดเน้นสอบ</a>{QUIZ_NAV}{"".join(nav)}</nav>
<main>
{HOME}
{QUIZ_BODY}
{"".join(body)}
</main>
{RANK}
</div>
<div id="lb"><img alt=""></div>
<script id="imgdata" type="application/json">{json.dumps(imgs)}</script>
<script id="quizdata" type="application/json">{QUIZ_JSON}</script>
<script>{JS}</script>
</body>
</html>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(page)
print("wrote", OUT, round(len(page.encode("utf-8")) / 1e6, 2), "MB;", len(imgs), "images;",
      sum(len(c["sections"]) for c in CLIPS), "sections")
