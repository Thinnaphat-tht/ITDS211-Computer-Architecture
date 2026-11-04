# คลิปที่ 1: 2026-10-25 18-05-55 (37:37) ติวทบทวน Ch1-3
CLIP = {
    "id": "v1",
    "file": "2026-10-25 18-05-55",
    "dur": "37:37",
    "title": "ทบทวนบทที่ 1–3",
    "scope": "Ch01 Basic Architecture · Ch02 Model/Bus/Interrupt · Ch03 Data Representation & Assembly",
    "intro": """<p>อาจารย์เปิดคลาสพิเศษ (Special Class &amp; Happy Hour) แล้วไล่ทบทวนสไลด์ Ch1–3 ตามลำดับ</p>
<div class="box exam"><ul>
<li>อาจารย์จะ <b>"แกล้งนิดๆ หน่อยๆ สัก 2–3 ข้อ"</b> นอกนั้นทุกอย่าง <b>อยู่ในสไลด์และอาจอยู่ใน assignment</b></li>
<li>ข้อสอบ Assembly เป็น <b>ข้อสอบแบบเลือกตอบ (ช้อยส์)</b> ไม่ต้องเขียนโค้ด</li>
<li>Data Representation (<b>Sign-Magnitude</b> กับ <b>2's Complement</b>) <b>"จะมีข้อนี้แน่ๆ"</b> และต้องทำได้เต็ม</li>
</ul></div>""",
    "sections": [
        {
            "time": "00:34", "ch": "บทที่ 1: สถาปัตยกรรมพื้นฐานและประสิทธิภาพ",
            "title": "องค์ประกอบของคอมพิวเตอร์และ CPU (Components)",
            "slides": [("Chapter01", 13), ("Chapter01", 14)],
            "body": """<ul>
<li>องค์ประกอบหลักของคอมพิวเตอร์: <b>CPU</b>, Input/Output, <b>Memory</b>, Storage, Motherboard, Power Supply</li>
<li>ภายใน CPU: <b>Control Unit</b>, <b>Arithmetic (ALU)</b>, <b>Registers</b> และ <b>Bus</b> สำหรับเชื่อมต่อ</li>
<li>อาจารย์บอกว่าเป็นเรื่อง "basic มากๆ" จดไว้ในโน้ตได้เลย</li>
</ul>""",
        },
        {
            "time": "01:35", "ch": None,
            "title": "ขั้นตอนการทำงานของ CPU (Machine Cycle)",
            "slides": [("Chapter01", 15)],
            "body": """<ul>
<li>อาจารย์พูดเสมอว่า CPU ทำงานเป็น "สเต็ป" (3 หรือ 5 สเต็ปแล้วแต่รุ่น/แบรนด์) แต่หลัก ๆ หนีไม่พ้น:
<ol><li><b>Fetch</b> ดึงคำสั่ง</li><li><b>Decode</b> ถอดรหัสว่าต้องทำอะไร แล้วเตรียมข้อมูล</li><li><b>Execute</b> ประมวลผล (บวก ลบ คูณ หาร)</li><li><b>Store</b> เก็บผลลัพธ์ลง Register หรือ Memory</li></ol></li>
<li>บางที่เรียกขั้นสุดท้ายว่า <b>Write back</b> ขึ้นกับประเภท/แบรนด์ของ CPU</li>
</ul>""",
        },
        {
            "time": "02:10", "ch": None,
            "title": "Register สำคัญใน CPU",
            "slides": [("Chapter01", 16)],
            "body": """<ul>
<li><b>PC (Program Counter)</b> เก็บ <b>ตำแหน่ง</b> ของคำสั่งที่จะประมวลผลถัดไป</li>
<li><b>IR (Instruction Register)</b> เก็บ <b>คำสั่งที่ Fetch มาแล้ว</b></li>
<li>กลุ่ม <b>Status / Flag register</b> เก็บสถานะ เช่น Overflow, Negative flag</li>
<li>อาจารย์บอกว่าส่วนนี้ "ไม่น่ามีประเด็น"</li>
</ul>""",
        },
        {
            "time": "02:44", "ch": None,
            "title": "ลำดับชั้นหน่วยความจำ (Pyramid) และ Cache",
            "slides": [("Chapter01", 17)],
            "body": """<ul>
<li>เป็นรูป <b>สามเหลี่ยมพีระมิด</b>: บนสุดเร็วสุดคือ <b>Register</b> → รองลงมาคือ <b>Cache</b> (พักข้อมูลจาก Memory ให้ CPU คุยได้เร็วขึ้น)</li>
<li>รายละเอียดของ Cache อาจารย์ให้ไปดูสไลด์ส่วนขยายภายหลัง (Ch04)</li>
<li>ส่วน overview ของ <b>multi-core / multi-thread</b> อยู่ในสไลด์ถัดไป อาจารย์บอกว่าจะกลับมาพูดอีกครั้ง</li>
</ul>""",
        },
        {
            "time": "03:54", "ch": None,
            "title": "Performance: เทียบความเร็วของ CPU",
            "slides": [("Chapter01", 36)],
            "body": """<ul>
<li>Performance = ความเร็ว/ประสิทธิภาพ ถ้าบอกว่า CPU A เร็วกว่า B กี่เท่า ให้เอา <b>Performance A ÷ Performance B</b></li>
<li>ในทางเวลาคือกลับด้าน: <b>Execution time ของ B ÷ Execution time ของ A</b></li>
<li>อาจารย์เรียกว่า "บัญญัติไตรยางศ์ง่ายๆ" แค่ <b>อ่านโจทย์ดีๆ</b>: เร็วกว่า = ใช้เวลาน้อยกว่า, ใช้เวลามากกว่า = ช้ากว่า</li>
</ul>
<div class="box formula">Performance<sub>A</sub> / Performance<sub>B</sub> = Execution time<sub>B</sub> / Execution time<sub>A</sub></div>""",
        },
        {
            "time": "05:00", "ch": None,
            "title": "Clock, CPU time และ CPI",
            "slides": [("Chapter01", 37), ("Chapter01", 41), ("Chapter01", 42)],
            "body": """<ul>
<li><b>Clock frequency (speed)</b> = 1 ÷ <b>Clock period</b> (คาบ)</li>
<li><b>CPU time</b> หาได้จาก CPU clock cycles ÷ clock rate</li>
<li><b>CPI</b> = Clock cycles per Instruction (อาจารย์ให้ "ดูดีๆ")</li>
<li>CPU time = <b>Instruction count × CPI × Cycle time</b> เมื่อเทียบสองเครื่อง ตัวแปร Instruction count ตัดทิ้งได้ (ถ้าไม่รู้ค่าก็ติดตัวแปรไว้ก่อน) แล้วหารกันเพื่อดูว่าเร็วกว่ากี่เท่า</li>
</ul>
<div class="box formula">CPU time = Instruction count × CPI × Cycle time<br>Frequency = 1 / Clock period</div>
<div class="box ex"><b>ตัวอย่างบนสไลด์ (CPI Example)</b>: A: cycle 250 ps, CPI 2.0 · B: cycle 500 ps, CPI 1.2 · ISA เดียวกัน<br>CPU time A = I × 2.0 × 250 = 500·I ps, CPU time B = I × 1.2 × 500 = 600·I ps → <b>A เร็วกว่า 1.2 เท่า</b></div>""",
        },
        {
            "time": "07:36", "ch": None,
            "title": "จบบทที่ 1 และช่วงเช็กคำถาม",
            "slides": [],
            "body": """<ul>
<li>อาจารย์เช็กว่าทุกคนตามทัน แล้วให้นักศึกษาช่วยอัดวิดีโอ (ระหว่าง 08:39–11:30 เป็นช่วงหาปุ่มอัด ไม่มีเนื้อหาวิชา)</li>
<li>ตอนไปสไลด์ที่ 2 อาจารย์ย้ำว่า <b>"สไลด์ที่ 1 พอจับได้นะว่าอาจารย์เน้นตรงจุดไหน"</b> และเรียกว่าเป็นฮินต์สุดๆ</li>
</ul>""",
        },
        {
            "time": "11:30", "ch": "บทที่ 2: แบบจำลองสถาปัตยกรรม ระบบบัส และอินเทอร์รัปต์",
            "title": "โมเดลคอมพิวเตอร์: Von Neumann vs Harvard",
            "slides": [("Chapter02", 3), ("Chapter02", 4)],
            "body": """<ul>
<li><b>Von Neumann</b>: Input → CPU → Output โดย <b>Memory เป็นก้อนเดียว เก็บทั้งคำสั่งและข้อมูล</b> (แบ่งกันภายใน)</li>
<li><b>Harvard</b>: Control Unit อยู่กลางคุยกับ ALU, <b>Data Memory</b> และ <b>Instruction Memory</b> ที่ <b>แยกกัน</b> พร้อม I/O</li>
<li>กลุ่ม Harvard ส่วนใหญ่เป็นตระกูล <b>Microcontroller</b></li>
<li>คำศัพท์รวม: "structure model ของคอมพิวเตอร์มี 2 ไทป์"</li>
</ul>""",
        },
        {
            "time": "13:04", "ch": None,
            "title": "Bus: Point-to-point vs Multipoint",
            "slides": [("Chapter02", 5), ("Chapter02", 6)],
            "body": """<ul>
<li>Bus แยกหน้าที่: <b>Address bus</b> (บอกตำแหน่งใน Memory), <b>Data bus</b> (ส่งข้อมูล), <b>Control bus</b> (สัญญาณเปิด/ปิด/เลือกอุปกรณ์ เช่น I/O)</li>
<li><b>Point-to-point</b>: แยกทุกหน้าที่ออกจากกัน ง่ายสุดแต่ <b>เปลืองเส้น</b> (Data ชุดหนึ่ง Address ชุดหนึ่ง Control ชุดหนึ่ง)</li>
<li><b>Multipoint</b>: ประหยัดเส้น เหมือน <b>ถนนไฮเวย์ (เส้นหลัก) + ถนนซอย</b> ที่แยกไปหา CPU/Memory/Disk/I/O แต่การสื่อสารซับซ้อนขึ้น จึงต้องมี <b>โปรโตคอลควบคุม</b></li>
</ul>""",
        },
        {
            "time": "14:40", "ch": None,
            "title": "Bus Arbitration 4 แบบ",
            "slides": [("Chapter02", 7)],
            "body": """<ol>
<li><b>Daisy chain</b>: ให้สิทธิ์ตาม <b>priority</b> คนสูงสุดได้ใช้ก่อน ไม่ต้องคิดเยอะ (นิยมสุด ใช้กันถึงทุกวันนี้) ปกติ CPU สูงสุด ตามด้วย Memory <b>ข้อเสีย: อุปกรณ์ priority ต่ำ (เช่น I/O) แทบไม่ได้ใช้ bus</b></li>
<li><b>Centralized parallel</b>: แต่ละอุปกรณ์ต่อตรงเข้าวงจรควบคุมกลาง (arbitration circuit) มีตัวกลางคอย observe ว่าใครจะใช้</li>
<li><b>Distributed with self-detection</b>: ไม่มีตัวกลาง <b>อุปกรณ์ตัดสินกันเอง</b> ต้องเช็กเองว่ามีใครส่งอยู่ไหม</li>
<li><b>Distributed with collision-detection</b>: เช็กเองเหมือนข้อ 3 แต่เพิ่มวงจรตรวจจับการชน ถ้าข้อมูลชนกันเสียหาย <b>ส่งซ้ำ (retransmit)</b></li>
</ol>""",
        },
        {
            "time": "17:25", "ch": None,
            "title": "Hardware vs Software Approaches",
            "slides": [("Chapter02", 8), ("Chapter02", 9)],
            "body": """<ul>
<li><b>Programming in hardware</b>: ข้อมูลกับ logic ถูกสร้างเป็น <b>วงจร</b> ใส่ข้อมูลเข้าไปก็ได้คำตอบออกมา ทำได้ <b>เร็ว</b> เพราะออกแบบมาเฉพาะงาน แต่ <b>ล็อกตายตัว</b></li>
<li><b>Software (general purpose)</b>: มีชุดคำสั่งบอกว่าจะให้ทำอะไร <b>ยืดหยุ่น</b> ต้อง "คิด" ก่อนทุกครั้งว่าคำสั่งนี้ต้องทำอะไร</li>
<li>เปรียบเทียบของอาจารย์: <b>ร้านอาหารตามสั่ง</b> (สั่งได้ทุกเมนู) vs <b>เครื่องที่ถูกโปรแกรมมาให้ผัดข้าวผัดอย่างเดียว</b></li>
<li>ฝั่งซอฟต์แวร์มองเป็น <b>ลำดับคำสั่ง</b> ที่ทำทีละบรรทัด ส่วน component ในสถาปัตยกรรมคือ <b>ฮาร์ดแวร์/วงจร</b> เช่น CPU, I/O</li>
</ul>""",
        },
        {
            "time": "20:39", "ch": None,
            "title": "Register ที่ใช้คุยกับ Memory และ I/O",
            "slides": [("Chapter02", 10)],
            "body": """<ul>
<li><b>MAR (Memory Address Register)</b>: เก็บ <b>Address</b> ของตำแหน่งใน Memory ที่จะคุยด้วย</li>
<li><b>MBR (Memory Buffer Register)</b>: เก็บ <b>data</b> ที่โหลดออกจาก Memory หรือที่กำลังจะเขียนเข้า Memory</li>
<li><b>IOAR (I/O Address Register)</b>: เก็บ Address ของอุปกรณ์ I/O (เช่น 001 = คีย์บอร์ด, 002 = อีกตัว ตามที่โปรแกรมแม็ปไว้)</li>
<li><b>IOBR (I/O Buffer Register)</b>: เก็บข้อมูลที่รับมาจาก I/O</li>
</ul>""",
        },
        {
            "time": "22:51", "ch": None,
            "title": "ตัวอย่างการไหลของคำสั่ง (Example of Program Execution)",
            "slides": [("Chapter02", 14)],
            "body": """<ul>
<li>Fetch + Decode ไปด้วยกัน แล้ว Execute</li>
<li>ตัวอย่างบนสไลด์: <b>PC = 300</b> → ไปดู Memory ตำแหน่ง 300 ได้ <b>1940</b> → โหลดเข้า <b>IR</b></li>
<li>ดู instruction format: <b>4 บิตบน = opcode</b> → <code>0001</code> หมายถึง <b>Load AC จาก Memory</b> ส่วนที่เหลือ (940) คือ Address</li>
<li>Memory ตำแหน่ง 940 มีค่า <code>0003</code> → โหลดมาใส่ใน <b>AC</b> ได้ 0003</li>
<li>อาจารย์บอกว่านี่คือ assignment ที่เคยทำ ให้เข้าใจว่า <b>opcode บอกว่าทำอะไร</b> ส่วนที่เหลือเป็น Address ของข้อมูล</li>
</ul>""",
        },
        {
            "time": "25:36", "ch": None,
            "title": "Interrupt: ขั้นตอนเมื่อมีการขัดจังหวะ",
            "slides": [("Chapter02", 32)],
            "body": """<p>ปกติคำสั่งทำงาน Fetch → Decode → Execute วนไปเรื่อย ๆ จนกว่าจะมี <b>Interrupt</b> มาขัดจังหวะ อาจารย์ย้ำว่า "จำไว้เลย":</p>
<ol>
<li><b>เซฟค่า</b> ตัวแปรและ Register ปัจจุบันไว้ก่อน</li>
<li>ดูว่าใครเป็นคนเรียก โดยเปิด <b>Interrupt Vector table</b> (เช่น Interrupt เบอร์ 003 = คีย์บอร์ด) เพื่อหา <b>ISR Address</b></li>
<li>เอา Address นั้นใส่ใน <b>PC</b> แล้วกระโดดไปทำ <b>ISR (Interrupt Service Routine)</b></li>
<li>ทำเสร็จ <b>Restore</b> ค่า Register ที่เซฟไว้ แล้วกระโดดกลับไปทำงานเดิมต่อ</li>
</ol>
<p class="note">อาจารย์บอกว่าตอนท้ายสไลด์มีเรื่อง Interrupt อีกครั้งแบบจริงจัง</p>""",
        },
        {
            "time": "27:45", "ch": None,
            "title": "Sequential vs Nested Interrupt",
            "slides": [("Chapter02", 44)],
            "body": """<ul>
<li><b>Sequential</b>: Interrupt เกิด → ไปทำ → กลับมา → เกิดอีกครั้ง → ไปทำ → กลับมา ตามลำดับ</li>
<li><b>Nested interrupt</b>: ระหว่างทำ service routine ของ Interrupt X มี Interrupt Y <b>ซ้อน</b>เข้ามา → ต้อง <b>เซฟสถานะของ X</b> ก่อนไปทำ Y เสร็จแล้ว <b>คืนค่าของ X</b> ทำ X ต่อจนจบ แล้วค่อย return กลับโปรแกรมปกติ</li>
<li><b>ซ้อนได้กี่ชั้นขึ้นกับสถาปัตยกรรม CPU</b> ของแต่ละแบรนด์ ว่ามี Register ให้เซฟค่าจากการ Interrupt กี่ชุด (มี 2 ชุด = ซ้อนได้ 2 ที) ถ้าซ้อนเกินกว่าที่ Register เก็บได้ก็ซ้อนต่อไม่ได้</li>
<li>Interrupt คือสิ่งที่ <b>ขัดขวางการทำงานแบบ sequence</b> ของ CPU</li>
</ul>""",
        },
        {
            "time": "30:54", "ch": "บทที่ 3: การแทนข้อมูลและภาษาแอสเซมบลี",
            "title": "Data Representation: Sign-Magnitude และ 2's Complement",
            "slides": [("Chapter03", 10), ("Chapter03", 18)],
            "body": """<div class="box exam"><b>"จะมีข้อนี้แน่ๆ บอกไว้เลย"</b> เป็นข้อคำนวณ <b>Sign-Magnitude</b> กับ <b>2's Complement</b> อาจารย์ไม่ลงรายละเอียดในคลาสนี้ ให้ไปดู <b>assignment</b> ข้อนี้ต้องทำให้ได้เต็ม เพราะเหมือนใน assignment</div>
<ul>
<li>ต้องรู้ว่า <b>Sign-Magnitude บวกลบกันอย่างไร</b></li>
<li><b>2's Complement</b>: เวลาเอามาลบกัน ทำให้เป็น 2's Complement โดย <b>กลับบิต (invert) แล้วบวก 1</b></li>
</ul>""",
        },
        {
            "time": "31:55", "ch": None,
            "title": "Assembly: ข้อสอบเป็นช้อยส์ ไม่ต้องเขียนโค้ด",
            "slides": [("Chapter03", 46)],
            "body": """<ul>
<li>มีคนถามว่า Assembly ออกอย่างไร อาจารย์ตอบว่า <b>ข้อสอบเป็นช้อยส์ ไม่ได้ให้เขียนโค้ด</b> ต้องเข้าใจเพียงว่าคำสั่ง <b>ทำอะไร</b></li>
<li>ตัวอย่าง: <code>ADD A, B, C</code> = เอา <b>B บวก C แล้วเก็บใน A</b></li>
<li>อาจารย์ <b>ไม่ได้เจาะจงว่าเป็น RISC-V</b> ไม่ได้ระบุว่าต้องเป็น MIPS, ARM หรือตระกูลไหน เป็นแค่ความรู้ทั่วไป ไม่ต้องไปท่องเฉพาะเจาะจงตระกูล</li>
</ul>""",
        },
        {
            "time": "32:59", "ch": None,
            "title": "Endianness: Big-Endian vs Little-Endian",
            "slides": [("Chapter03", 51)],
            "body": """<ul>
<li>มี 2 ไทป์ที่เคยคุยกัน คือ <b>Big-Endian</b> กับ <b>Little-Endian</b> (สลับกันแค่นี้เอง)</li>
<li>ตามที่อาจารย์อธิบาย (เรียงบนกระดาษซ้าย–ขวา เช่น 8 บิต 0–7): <b>Little-Endian = บิต 0 (บิตล่าง/น้อยสุด) อยู่ขวามือ</b> ส่วน <b>Big-Endian = บิต 0 อยู่ซ้ายมือ</b></li>
<li>เวลาเขียนเลขฐาน 16 ที่เราคุ้นเคย มักคุ้นกับแบบ Little-Endian มากกว่า แต่ <b>ในโลกจริงมีทั้งสองค่าย</b></li>
</ul>
<p class="note">ผมเสริมจากสไลด์: สไลด์นิยามด้วย <b>byte address</b> ดูรูป address mapping ด้านล่างประกอบ (ไม่ใช่คำพูดของอาจารย์)</p>""",
        },
        {
            "time": "34:03", "ch": None,
            "title": "คำสั่ง Assembly พื้นฐาน: LOAD / STORE / ADD / ADDI",
            "slides": [("Chapter03", 55)],
            "body": """<ul>
<li><b>LOAD</b> (บางที่เขียน LD, LOD): เอาค่าจาก <b>Memory → Register</b></li>
<li><b>STORE</b> (ST, STOR): ตรงข้าม เอาจาก <b>Register → Memory</b></li>
<li><b>ADD</b>: บวกธรรมดา</li>
<li><b>ADDI</b>: แทนที่จะบวก Register 2 ตัว จะ <b>บวก Register กับค่าคงที่ (immediate)</b> เช่น เอา x22 + 4 แล้วเก็บใส่ x22</li>
</ul>
<div class="box ex"><code>addi x22, x22, 4</code> = x22 ← x22 + 4</div>""",
        },
        {
            "time": "35:10", "ch": None,
            "title": "รูปแบบคำสั่ง (Instruction Format): R-format และ I-format",
            "slides": [("Chapter03", 58), ("Chapter03", 60)],
            "body": """<ul>
<li>ถ้าข้อสอบออก จะ <b>มีแผนภาพ (chart) ให้</b> เพื่อบอกว่า opcode คืออะไร</li>
<li><b>7 บิตล่าง = opcode</b> บอกว่าเป็นคำสั่งบวก/ลบ/คูณ/หาร → มี opcode ได้ <b>2<sup>7</sup></b> แบบ</li>
<li><b>rs1</b> = source register ตัวที่ 1, <b>rs2</b> = source ตัวที่ 2, <b>rd</b> = destination register ทั้ง 3 ตัว <b>ละ 5 บิต</b> → มี Register ได้ <b>2<sup>5</sup></b> ตัว</li>
<li>ตัวอย่างที่อาจารย์ยก: <code>add x9, x20, x21</code> (เอา Register 20 บวก 21 เก็บใน 9) แปลงเป็น machine code: opcode = 51 (คำสั่งบวก), rd = 9, rs1 = 20, rs2 = 21</li>
<li><b>I-format</b>: ใช้ <b>12 บิตบน</b> เป็นค่าคงที่ (immediate) สำหรับคำสั่งที่มีค่าคงที่</li>
<li>คำสั่งอื่นที่อาจเจอ: <b>OR</b> (OR ระดับบิต), <b>Exclusive-OR (XOR)</b> เป็น exclusive ธรรมดา</li>
</ul>
<p class="note">ซับของคลิปนี้จบที่ 37:32 ตรงช่วงที่อาจารย์กำลังพูดถึงคำสั่งที่ "น่าสนใจ" ต่อ ส่วนที่เหลือไม่มีข้อมูล</p>""",
        },
    ],
}
