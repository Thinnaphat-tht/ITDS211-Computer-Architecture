# คลิปที่ 2: 2026-10-25 18-50-07 (26:51) ต่อจากคลิปที่ 1
CLIP = {
    "id": "v2",
    "file": "2026-10-25 18-50-07",
    "dur": "26:51",
    "title": "Assembly (ต่อ) และบทที่ 4 Memory / Cache",
    "scope": "Ch03 ส่วนท้าย (Logic, Branch, Procedure) · Ch04 Memory Hierarchy และ Cache",
    "intro": """<p>คลิปนี้เริ่มกลางคลาส (ต่อจากคลิปที่ 1) ปิด Ch03 แล้วเข้า Ch04 เน้น <b>Cache</b> เป็นหลัก</p>
<div class="box exam"><ul>
<li>ส่วนที่เป็น <b>self study</b> ของ RISC-V (รายละเอียดเฉพาะของ RISC-V ที่อาจารย์ทิ้งไว้ให้อ่านเอง) <b>ไม่ออกสอบ</b></li>
<li>ใน Ch04 ให้ <b>จำรูปพีระมิดหน่วยความจำ</b> และอาจารย์ "เน้นเรื่องของ Cache"</li>
</ul></div>
<p class="note">ซับของคลิปนี้มีถึง 25:00 จากความยาว 26:51 ส่วนท้าย (ประมาณ 1 นาที 51 วินาที) ไม่มีข้อมูล</p>""",
    "sections": [
        {
            "time": "00:09", "ch": "บทที่ 3 (ต่อ): ภาษา Assembly",
            "title": "Logical Operations และ Shift",
            "slides": [("Chapter03", 63)],
            "body": """<ul>
<li>คำสั่ง Logic: <b>AND, OR, XOR</b> เอาค่าใน Register มา AND / OR / Exclusive-OR กัน "ไม่ยาก"</li>
<li><b>Shift left</b> = เลื่อนบิตไปทางซ้ายทีละตำแหน่ง ตีความได้ว่าเป็น <b>การคูณ</b></li>
<li><b>Shift right</b> = เลื่อนไปทางขวา ตีความได้ว่าเป็น <b>การหาร</b></li>
</ul>""",
        },
        {
            "time": "01:14", "ch": None,
            "title": "Branch (การกระโดดตามเงื่อนไข)",
            "slides": [("Chapter03", 68)],
            "body": """<ul>
<li>คำสั่งกระโดดมี <b>jump</b> และ <b>branch</b> ส่วน branch จะ <b>เช็กเงื่อนไขก่อน</b> ใช้เวลาเขียนลูป</li>
<li>4 ตัวที่อาจารย์ชี้ว่าน่าสนใจ:
<ul>
<li><code>beq</code> (branch equal): ถ้าค่าใน register 1 กับ 2 <b>เท่ากัน</b> กระโดดไป L1</li>
<li><code>bne</code> (branch not equal): กระโดดเมื่อ <b>ไม่เท่ากัน</b></li>
<li><code>blt</code> (less than): กระโดดเมื่อ rs1 <b>น้อยกว่า</b> rs2</li>
<li><code>bge</code> (greater than or equal): กระโดดเมื่อ rs1 <b>มากกว่าหรือเท่ากับ</b> rs2</li>
</ul></li>
</ul>""",
        },
        {
            "time": "02:19", "ch": None,
            "title": "Procedure = ฟังก์ชัน และ Software Interrupt",
            "slides": [("Chapter03", 80), ("Chapter03", 81)],
            "body": """<ul>
<li><b>Procedure</b> คือฟังก์ชัน เมื่อโปรแกรมเรียกไปยัง procedure อื่น เปรียบเหมือน <b>software interrupt</b> (ขัดจังหวะโดยซอฟต์แวร์เอง)</li>
<li>ต้อง <b>save ค่าทั้งหมดลง stack</b> ก่อนกระโดดไป เมื่อทำ procedure เสร็จแล้วกลับมา ก็ <b>return ค่าจาก stack</b> เข้าไป</li>
<li>อาจารย์บอกว่า ส่วนที่เหลือของ Assembly "ไม่น่ามีอะไร"</li>
</ul>
<div class="box exam"><b>Self study ไม่ออกสอบ:</b> ส่วนรายละเอียดเฉพาะของ RISC-V ที่อาจารย์ทิ้งไว้ให้ ถ้าสนใจค่อยไปอ่านเพิ่มเอง "ตัวนี้ไม่ได้มีออก"</div>""",
        },
        {
            "time": "04:00", "ch": "บทที่ 4: ระบบหน่วยความจำ (Memory)",
            "title": "พีระมิดหน่วยความจำ (Memory Hierarchy)",
            "slides": [("Chapter04", 6)],
            "body": """<div class="box exam">อาจารย์ย้ำ: <b>"ให้จำรูปพีระมิดเอาไว้"</b></div>
<ul>
<li><b>ยอดพีระมิด</b>: ทำงานเร็ว แต่ <b>แพง</b> จึงเก็บได้น้อย</li>
<li><b>ฐานพีระมิด</b>: ทำงานช้า <b>ราคาถูก</b> เก็บได้เยอะมาก</li>
<li>เรียงจากบนลงล่าง: <b>Register</b> → <b>Cache</b> → <b>Main memory</b> → (นอกบอร์ด) Magnetic disk, CD-ROM, DVD, Blu-ray → <b>Magnetic tape</b></li>
<li><b>Magnetic tape</b> ราคาถูกมาก ใช้ใน big data center เป็น <b>offline storage</b> เก็บได้มหาศาล</li>
</ul>""",
        },
        {
            "time": "05:36", "ch": None,
            "title": "Cache: ทำหน้าที่คั่นระหว่าง CPU กับ Main Memory",
            "slides": [("Chapter04", 7)],
            "body": """<ul>
<li>Main memory <b>ช้า</b> ถ้า CPU เรียกใช้บ่อยจะติดขีดจำกัด จึงสร้าง <b>Cache</b> เป็นหน่วยความจำเร็วๆ มาคั่นกลาง</li>
<li>Cache เก็บ <b>ข้อมูลที่ใช้บ่อย/ใช้ซ้ำ</b> และเตรียมโค้ดที่จะรันไว้ จึงไม่ต้องเสียเวลา access Memory</li>
<li>มีหลายระดับ <b>L1, L2, L3</b> (กี่ level ขึ้นกับงบ/รุ่นของ CPU)</li>
<li><b>L1</b> อยู่ชิด CPU และอยู่ในก้อนเดียวกัน ส่วน <b>L2 / L3</b> อยู่ออกมาจากตัว CPU</li>
</ul>""",
        },
        {
            "time": "07:12", "ch": None,
            "title": "Hit และ Miss",
            "slides": [("Chapter04", 8)],
            "body": """<ul>
<li><b>Hit</b> = เปิดดูแล้ว <b>เจอ</b>ข้อมูลใน cache</li>
<li><b>Miss</b> = <b>ไม่เจอ</b> → ไปเอาข้อมูลจริงจาก <b>main memory</b> มาใส่ cache แล้วค่อยส่งให้ CPU ใช้</li>
</ul>""",
        },
        {
            "time": "07:43", "ch": None,
            "title": "เทคโนโลยีหน่วยความจำ: SRAM, DRAM, Flash, Disk",
            "slides": [("Chapter04", 9)],
            "body": """<ul>
<li><b>SRAM (Static RAM)</b>: ใช้ transistor เปิด-ปิด (on-off) แค่ไม่กี่ตัว <b>เร็วกว่า DRAM เกือบ 100 เท่า</b> แต่ราคาแพงกว่า</li>
<li><b>DRAM (Dynamic RAM)</b>: transistor น้อยกว่า เก็บข้อมูลเป็น <b>ประจุใน capacitor</b> ต้องคอยชาร์จประจุอยู่ตลอด จึง <b>ช้ากว่า</b> แต่ <b>ถูกกว่า</b></li>
<li><b>Flash</b> (NOR gate หรือ NAND gate): เก็บ logic 0/1 ด้วย transistor ใช้เป็น storage ทั่วไป</li>
<li><b>Hard disk</b>: จุได้เยอะกว่า flash เขียนข้อมูลด้วย <b>magnetic</b> (ไปดูรายละเอียดอีกครั้งในบท storage)</li>
</ul>
<table><tr><th>ชนิด</th><th>ความเร็ว</th><th>ราคา / GB (ตามสไลด์)</th></tr>
<tr><td>SRAM</td><td>0.5–2.5 ns</td><td>$2000–$5000</td></tr>
<tr><td>DRAM</td><td>50–70 ns</td><td>$20–$75</td></tr>
<tr><td>Magnetic disk</td><td>5–20 ms</td><td>$0.20–$2</td></tr></table>
<p class="note">ตัวเลขในตารางมาจากสไลด์ Memory Technology (ไม่ใช่คำพูดของอาจารย์)</p>""",
        },
        {
            "time": "10:22", "ch": None,
            "title": "Direct-Mapped Cache: หลักการ",
            "slides": [("Chapter04", 23)],
            "body": """<ul>
<li>cache มีหลักการหลัก ๆ 2–3 แบบ แบบแรกที่ง่ายสุดคือ <b>direct-mapped</b></li>
<li>ตำแหน่งใน cache = <b>block address modulo จำนวนบล็อกใน cache</b></li>
<li>ตัวอย่าง: cache 8 บล็อก (index 000–111) → เอา block address <b>mod 8</b> ก็คือดู <b>3 บิตล่าง</b> เป็น index</li>
<li><b>ข้อดี</b>: ง่าย · <b>ข้อเสีย</b>: ตำแหน่งเดียวกันมีหลายเลขที่อยากเข้ามาอยู่ (เช่น ตำแหน่ง 1 กับ 11 ลงท้าย 1 เหมือนกัน) จึงแย่งกันได้</li>
</ul>
<div class="box formula">Cache index = (Block address) modulo (#Blocks in cache)</div>""",
        },
        {
            "time": "12:30", "ch": None,
            "title": "ตัวอย่าง Direct-Mapped: Tag, Index, Valid bit",
            "slides": [("Chapter04", 26), ("Chapter04", 28), ("Chapter04", 29), ("Chapter04", 30)],
            "body": """<ul>
<li>สไลด์: cache 8 บล็อก, 1 word/block, direct-mapped เริ่มต้น <b>cache ว่างเปล่า</b> (Valid = N)</li>
<li>แยก address: ตัวอย่าง <b>10110</b> (= ที่ 22): <b>2 บิตบน = Tag</b> (10) · <b>3 บิตล่าง = Index</b> (110)</li>
<li>ครั้งแรกที่ขอ <b>22</b> → <b>Miss แน่นอน</b> (cache ว่าง) → ไปเอาจาก main memory เขียนลง cache ช่อง 110, ตั้ง <b>V = Y</b>, ใส่ tag 10 แล้วส่งข้อมูลให้ CPU</li>
<li>ขอ <b>26</b> (11010): Miss เหมือนกัน → เก็บที่ index 010, tag 11</li>
<li>ขอ <b>22 และ 26 อีกครั้ง</b> → มีข้อมูลแล้ว จึง <b>Hit</b> ไม่ต้องไป main memory</li>
<li>ขอ <b>16</b> (10 000) Miss, <b>3</b> (00 011) Miss, ขอ <b>16 ซ้ำ</b> = Hit</li>
<li><b>ขอ 18</b> (10 010): index 010 มีข้อมูลเดิมอยู่ แต่ <b>tag ไม่ตรง</b> (เดิม 11 ใหม่ 10) → <b>Miss</b> แล้วเขียนทับ</li>
<li>วิธีเช็กว่า hit หรือ miss: ดู <b>Index</b> → เทียบ <b>Tag</b> → ดูว่า <b>V (Valid)</b> เป็น Y หรือไม่</li>
<li>ถ้ามี index (บล็อก) เยอะ โอกาสเจอ (hit) ก็มากขึ้น</li>
</ul>""",
        },
        {
            "time": "16:52", "ch": None,
            "title": "คำนวณ Block address / Block number (บล็อกใหญ่ขึ้น)",
            "slides": [("Chapter04", 32)],
            "body": """<ul>
<li>โจทย์ตัวอย่างบนสไลด์: cache <b>64 บล็อก</b>, บล็อกละ <b>16 ไบต์</b> ถามว่า <b>address 1200</b> ไปอยู่บล็อกที่เท่าไร</li>
<li>ขั้นที่ 1: <b>Block address = ⌊1200 / 16⌋ = 75</b></li>
<li>ขั้นที่ 2: <b>Block number = 75 modulo 64 = 11</b></li>
</ul>
<div class="box formula">Block address = ⌊ address / (bytes per block) ⌋<br>Block number = Block address modulo (number of blocks)</div>
<p class="note">ซับของ Gemini ถอดตัวเลขกลางทางสลับกัน (ได้ยินเป็น 17/75) ผมยึดตัวเลขตามสไลด์ที่อาจารย์เปิดอยู่ ซึ่งสอดคล้องกับคำตอบสุดท้ายที่อาจารย์บอก "ประมาณ 11"</p>""",
        },
        {
            "time": "17:55", "ch": None,
            "title": "Write policy: Write-through / Write-back / Write-allocation",
            "slides": [("Chapter04", 36), ("Chapter04", 37)],
            "body": """<ul>
<li>เมื่อ miss ต้องไปเอาข้อมูลจาก main memory เขียนลง cache แล้วส่งให้ CPU:
<ul>
<li><b>Write-through</b>: เขียนลง cache แล้ว <b>ส่งให้ CPU เลย</b> (ตามคำอธิบายของอาจารย์)</li>
<li><b>Write-back</b>: ส่งข้อมูลให้ CPU <b>ก่อน</b> แล้วค่อย <b>อัปเดตบล็อกใน cache ทีหลัง</b></li>
<li><b>Write-allocation</b>: อีกทางเลือกหนึ่งของ write-through</li>
</ul></li>
<li>เรื่องเล่าของอาจารย์: เมื่อ 10 กว่าปีก่อนมีงานวิจัย (paper) แข่งกันเรื่องกลไกการเขียนค่าเยอะมาก เพราะ cache สมัยนั้นยังไม่เร็ว แต่ <b>ปัจจุบัน transistor เล็กลงเหลือระดับ 2–4 นาโนเมตร</b> memory เร็วและจุได้มากขึ้น เรื่องความเร็วไม่ใช่ปัญหาหนัก algorithm การเขียนค่าเหล่านี้จึงค่อย ๆ หายไป เพราะ "ลงทุนทำเยอะ แต่ improvement ไม่มีนัยสำคัญ"</li>
<li>ปัจจุบันเน้นแค่ <b>ยัดโค้ดที่ execute บ่อยๆ เข้า cache L1 ให้ได้เยอะที่สุด</b> ทุกอย่างก็ hit และ performance ดีขึ้น</li>
</ul>
<div class="box warn">อาจารย์เล่าส่วนนี้เป็นประวัติ/แนวโน้ม ไม่ได้บอกว่าเป็นจุดเน้นสอบ แต่ <b>ควรรู้นิยามของสามคำ</b> เพราะเป็นศัพท์ในสไลด์</div>""",
        },
        {
            "time": "21:26", "ch": None,
            "title": "Cache อีก 2 ชนิด: Set-Associative และ Fully-Associative",
            "slides": [("Chapter04", 46), ("Chapter04", 47)],
            "body": """<ul>
<li>นอกจาก direct-mapped ยังมี <b>set-associative</b> กับ <b>fully-associative</b></li>
<li>แทนที่จะให้ index 0 เก็บได้ <b>1 ชุด</b> ก็ให้เก็บได้หลายชุดเป็น <b>set</b>:
<ul><li><b>2-way</b> เก็บ 2 · <b>4-way</b> เก็บ 4 · <b>8-way</b> เก็บ 8 · 16-way เก็บ 16</li></ul></li>
<li>อาจารย์สรุปว่า "ไม่ได้ฉลาดอะไรมากขึ้น" แค่ <b>ขยายจำนวนที่เก็บใน index เดียวกัน เพื่อเพิ่มความน่าจะเป็นของการ hit</b></li>
<li>จึงทำให้ set-associative มีโอกาส hit <b>มากกว่า</b> direct-mapped แบบ 1 ต่อ 1</li>
</ul>""",
        },
        {
            "time": "24:28", "ch": None,
            "title": "Associativity เท่าไรถึงคุ้ม (How Much Associativity)",
            "slides": [("Chapter04", 50)],
            "body": """<ul>
<li>มีการวิจัยดูว่าเพิ่มทีละ 2, 4, 8, 16 แล้ว performance ไปถึงไหน: ความน่าจะเป็นที่ hit <b>ดีขึ้นแต่ได้น้อยลงเรื่อย ๆ</b> (diminishing returns)</li>
<li>ตัวเลขบนสไลด์ (miss rate): <b>1-way 10.3% · 2-way 8.6% · 4-way 8.3% · 8-way 8.1%</b></li>
</ul>
<p class="note">ซับหยุดที่ 25:00 จากภาพในคลิป ช่วง 25:30 อาจารย์ยังอยู่ที่สไลด์นี้ และเมื่อถึง 26:20 เปิดสไลด์ <b>Dependability Measures</b> (MTTF, MTTR, Availability) คำพูดช่วง 25:00–26:51 ไม่มีข้อมูล จึงสรุปไม่ได้ว่าอาจารย์พูดอะไร</p>""",
        },
    ],
}
