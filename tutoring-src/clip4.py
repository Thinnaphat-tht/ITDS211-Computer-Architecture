# คลิปที่ 4: 2026-10-25 19-32-45 (38:47) Ch05 ปิดท้าย + Ch06 Storage + Ch07 Pipeline + Ch08 Parallel
# หมายเหตุ: เวลาในซับของ Gemini คลาดเคลื่อน (ช่วงท้ายคลาดถึง ~7 นาที) เวลาในไฟล์นี้อ้างจากสไลด์ที่ปรากฏในคลิป (ประมาณ ±1 นาที)
CLIP = {
    "id": "v4",
    "file": "2026-10-25 19-32-45",
    "dur": "38:47",
    "title": "I/O (ปิดท้าย) · Storage · Pipeline · Parallel/GPU",
    "scope": "Ch05 ปิดท้าย · Ch06 Storage (HDD, RAID, SSD) · Ch07 Pipeline & Hazards · Ch08 Parallel Processors/GPU",
    "intro": """<p>คลิปยาวที่สุด อาจารย์ไล่ปิด 4 บทสุดท้ายในคลิปเดียว และปิดท้ายด้วย Q&amp;A</p>
<div class="box exam"><ul>
<li>Ch06 <b>Storage "ออกไม่เยอะมาก"</b> ตรงไปที่ <b>Hard Disk</b></li>
<li>คำถามเรื่อง I/O ที่อ้างถึง assignment (USB, SCSI, Thunderbolt, InfiniBand) เป็นแนว <b>basic ทั่วไป ไม่ยาก</b></li>
<li>ปิดท้ายอาจารย์บอกว่า <b>"ประมาณนี้ที่อาจารย์จะออกในข้อสอบ"</b> และยืนยันกับนักศึกษาว่าข้อสอบเป็น <b>multiple choice 60 ข้อ</b></li>
</ul></div>
<div class="box warn"><b>ข้อควรรู้เกี่ยวกับข้อมูลคลิปนี้:</b> เวลาในซับที่ Gemini ถอดคลาดเคลื่อนมากช่วงหลัง และช่วงท้ายคลิป (หลังประมาณ 32 นาทีในซับ) ถอดวนซ้ำข้อความเดิม ผมจึงเรียงเนื้อหาตามลำดับที่อาจารย์สอนจริง และใส่เวลาจากสไลด์ที่ปรากฏในวิดีโอ (ประมาณ) เนื้อหาช่วง Q&amp;A ท้ายคลิปสรุปจากข้อความที่ถอดได้</div>""",
    "sections": [
        {
            "time": "≈00:20", "ch": "บทที่ 5 (ปิดท้าย): I/O",
            "title": "ต่อพ่วง I/O เยอะๆ ด้วยตัวเลือก 8-to-1 (Multiplexer)",
            "slides": [("Chapter05", 20)],
            "body": """<ul>
<li>ตัวเลือกแบบ <b>8-to-1</b> คุยกับ I/O ได้ 8 ตัว เลือกมาได้ <b>1 ตัว</b></li>
<li>ถ้ามี I/O มากกว่า 8 ตัว เช่น <b>64 ตัว</b> ก็ใช้ <b>8 ชุด</b> ของ 8-to-1 แล้วใช้ 8-to-1 อีกตัวเลือกจากกลุ่มทั้ง 8 ให้เหลือ <b>1 ตัว</b> (ตรงกับสไลด์ Interrupt Controller แบบ master/slave)</li>
</ul>""",
        },
        {
            "time": "≈01:20", "ch": None,
            "title": "ทำไมปัจจุบันใช้ DMA เป็นหลัก",
            "slides": [("Chapter05", 26)],
            "body": """<ul>
<li>Programmed I/O และ Interrupt-driven I/O <b>ไปยุ่งกับ processor</b> จึง <b>ช้า</b></li>
<li><b>DMA</b> คุยกับ memory ได้ <b>ในทุก slot ของ processor cycle</b> (ก่อน fetch, หลัง decode, หลัง execute แทรกได้ตลอด)</li>
<li>ถ้า I/O จะ interrupt processor ตรง ๆ <b>processor จะถูกขัดจังหวะไม่ได้กลางทางที่กำลังทำงาน</b> ต้องรอให้ <b>จบ instruction cycle</b> ก่อน เช่นมี pipeline 4–5 stage ก็ต้องรอครบ 4–5 cycle</li>
<li>DMA จึงเร็วกว่า แทรกได้ตรง ๆ โดยไม่ต้องรอให้คำสั่งเสร็จ ปัจจุบัน I/O <b>ใช้ DMA เป็นส่วนใหญ่</b></li>
</ul>""",
        },
        {
            "time": "≈03:20", "ch": None,
            "title": "คำถามเรื่อง I/O จาก assignment: USB, SCSI, Thunderbolt, InfiniBand",
            "slides": [("Chapter05", 41), ("Chapter05", 45)],
            "body": """<div class="box exam">อาจารย์บอกว่าเนื้อหาตามชีทรายงานที่เพื่อนนำมาพรีเซนต์ จะออกเป็นคำถาม <b>แนวทั่วไป ไม่ยาก</b> เช่น:
<ul>
<li><b>USB</b> เป็นอย่างไร แตกต่างจาก <b>SCSI</b> อย่างไร</li>
<li><b>Thunderbolt</b> เป็นรูปแบบไหน</li>
<li><b>InfiniBand</b> ใช้กับอุปกรณ์ประเภทไหนโดยเฉพาะ → ใช้กับ <b>GPU ↔ memory ที่ต้องการความเร็วสูงสุด</b> (เพราะ GPU ทำงานเร็ว และต้องคุยกับ memory/CPU ให้เร็ว) เป็น I/O type แบบ <b>high speed สุด ๆ</b></li>
</ul></div>""",
        },
        {
            "time": "≈04:50", "ch": "บทที่ 6: Storage",
            "title": "Hard Disk: หลักการเขียน/อ่าน",
            "slides": [("Chapter06", 5), ("Chapter06", 6)],
            "body": """<ul>
<li>อาจารย์ย้ำว่า <b>storage ออกไม่เยอะมาก</b> เน้น <b>hard disk</b> ว่า <b>หลักการทำงาน/การใช้งาน</b> เป็นอย่างไร</li>
<li><b>เขียน</b>: จ่าย <b>กระแสไฟฟ้า</b>เข้าหัวเขียน (ขดลวด) → เกิด <b>สนามแม่เหล็ก</b> → ทำให้ <b>ทิศทางของอนุภาคแม่เหล็กบนผิวจาน</b> เรียงไปทางซ้ายหรือขวา แทนค่า <b>0 กับ 1</b></li>
<li><b>อ่าน</b>: หัวอ่านใช้ขดลวด <b>เหนี่ยวนำสัญญาณ</b> ดูว่าทิศไปทางซ้ายหรือขวา เพื่อแปลงเป็น 0 หรือ 1</li>
<li>HDD ประกอบด้วย <b>platter</b> หลายชั้น หัวอ่านเข้าไปเสียบตามจำนวนชั้น โดยทั่วไป <b>1 หัว ต่อ 1 ผิว</b></li>
</ul>""",
        },
        {
            "time": "≈06:30", "ch": None,
            "title": "การแบ่งพื้นที่จาน: แบบเก่า vs Multi-zone recording",
            "slides": [("Chapter06", 8)],
            "body": """<ul>
<li>แบบเก่า (a) แบ่งเหมือน <b>หั่นเค้ก</b> แล้วแต่ละ track แบ่งเป็น sector ข้อเสียคือ <b>ขนาด sector ไม่เท่ากัน</b></li>
<li>แบบ <b>Multi-zone recording</b> (b): ความหนาแน่นของข้อมูล / ขนาด sector ใกล้เคียงกัน <b>ดีกว่า</b></li>
<li>ปัจจุบัน hard disk ส่วนใหญ่ใช้ <b>multiple zone recording</b></li>
</ul>""",
        },
        {
            "time": "≈08:00", "ch": None,
            "title": "RAID 0–6",
            "slides": [("Chapter06", 17), ("Chapter06", 24), ("Chapter06", 26)],
            "body": """<table>
<tr><th>Level</th><th>ที่อาจารย์อธิบาย</th></tr>
<tr><td><b>RAID 0</b></td><td>เขียนข้อมูลเป็น <b>ชิ้นเล็ก ๆ กระจาย (striping)</b> ลงหลายดิสก์พร้อมกัน</td></tr>
<tr><td><b>RAID 1</b></td><td><b>เขียนข้อมูลชุดเดียวกันซ้ำลง 2 ดิสก์ (mirror)</b> เปลืองแต่ <b>ปลอดภัย</b> เพราะมีข้อมูลสำรอง (redundant)</td></tr>
<tr><td><b>RAID 2</b></td><td>เก็บ <b>parity bit</b> (ค่าตรวจสอบความถูกต้อง) ไว้ด้วย ใช้กู้ข้อมูลถ้าดิสก์เสียหาย</td></tr>
<tr><td><b>RAID 3</b></td><td>คล้าย parity แต่เก็บเป็น <b>ระดับ byte</b> และ parity อยู่ที่ <b>ดิสก์ตัวเดียว</b></td></tr>
<tr><td><b>RAID 4</b></td><td>เก็บเป็นระดับ <b>block</b> ร่วมกับ <b>parity disk แยกต่างหาก</b> → มีปัญหา <b>คอขวด (bottleneck)</b></td></tr>
<tr><td><b>RAID 5</b></td><td>block-level เหมือนเดิม แต่ <b>parity หมุนเวียน</b> กระจายทุกดิสก์ (แก้คอขวดของ RAID 4)</td></tr>
<tr><td><b>RAID 6</b></td><td>เหมือน RAID 5 แต่เก็บ <b>parity 2 ชุด</b> เพื่อตรวจ/กู้ข้อมูลได้ดีขึ้น</td></tr>
</table>""",
        },
        {
            "time": "≈10:30", "ch": None,
            "title": "SSD vs HDD และสื่อเก็บข้อมูลอื่น ๆ",
            "slides": [("Chapter06", 29), ("Chapter06", 34), ("Chapter06", 41)],
            "body": """<ul>
<li><b>SSD ดีกว่า HDD</b>: <b>เร็วกว่า</b> (performance ดี) และ <b>ใช้พลังงานน้อยกว่า</b> แต่ <b>ราคาแพงกว่า</b></li>
<li>Storage ที่ <b>ถูกและเก็บได้เยอะ</b>: <b>CD-ROM, DVD</b> (ข้อมูลทั่วไป)</li>
<li><b>Magnetic tape</b>: storage ที่ <b>ถูกที่สุด</b> (อาจารย์ย้ำอีกรอบ)</li>
</ul>
<div class="box ex"><b>คำถามจากนักศึกษา: CD กับ DVD ต่างกันอย่างไร</b><br>ทั้งสองเป็นแผ่นกลมเหมือนกัน แต่ <b>sector ของ CD ใหญ่กว่า DVD</b> ส่วน <b>DVD มีความหนาแน่น (density) มากกว่า</b> จึงเก็บข้อมูลได้มากกว่า (อาจารย์เปรียบกับแผ่นจานใน hard disk ที่แบ่งเป็น sector)</div>""",
        },
        {
            "time": "≈11:50", "ch": "บทที่ 7: Pipeline",
            "title": "แนวคิด Pipelining",
            "slides": [("Chapter07", 3), ("Chapter07", 4)],
            "body": """<ul>
<li>แทนที่จะทำ fetch → decode → execute → เขียนค่า <b>เรียงเป็น sequence</b> ใช้วิธี <b>แบ่งเป็น stage ย่อย</b> แล้วใช้ resource ไม่ให้ชนกันในเวลาเดียวกัน</li>
<li><b>ตัวอย่างของอาจารย์: ซักผ้า–อบผ้า–รีดผ้า–เก็บผ้า</b> แต่ละอย่างใช้ resource ต่างกัน จึงทำคำสั่ง 1 2 3 4 ที่ใช้ resource ไม่ตรงกันไปพร้อม ๆ กันได้</li>
<li>Stage แบ่งตามชนิด CPU (RISC-V, Arm, Intel ไม่เหมือนกัน) ตัวอย่างบนสไลด์: <b>IF, ID, EX, MEM, WB</b></li>
<li>ผลลัพธ์: ทำงาน <b>เร็วขึ้น</b> แต่เกิดปัญหา <b>3 เรื่อง (hazards)</b></li>
</ul>""",
        },
        {
            "time": "≈13:30", "ch": None,
            "title": "Hazard ที่ 1: Structural Hazard",
            "slides": [("Chapter07", 8), ("Chapter07", 9)],
            "body": """<ul>
<li>ปัญหา 3 แบบ: <b>structural hazard, data hazard, control hazard</b></li>
<li><b>Structural hazard</b> = <b>การใช้ resource ชนกัน</b> (conflict) ในเวลาเดียวกัน</li>
<li>วิธีแก้: <b>stall</b> = หยุด pipeline (เกิดช่องว่าง/bubble) จนกว่า resource จะว่าง แล้วจึงทำต่อ</li>
</ul>""",
        },
        {
            "time": "≈15:00", "ch": None,
            "title": "Hazard ที่ 2: Data Hazard และวิธีแก้ (Stall, Forwarding, Code Scheduling)",
            "slides": [("Chapter07", 10), ("Chapter07", 11), ("Chapter07", 13)],
            "body": """<p><b>Data hazard</b> = resource ไม่ได้ชน แต่ <b>ข้อมูลชน/ยังไม่พร้อม</b></p>
<div class="box ex">ตัวอย่างบนสไลด์: <code>add x19, x0, x1</code> ตามด้วย <code>sub x2, x19, x3</code><br><code>sub</code> ต้องใช้ x19 แต่ <code>add</code> ที่อยู่ก่อนหน้ายังไม่ทัน <b>เขียนค่าลง x19</b> (ยังไม่ถึง write back)</div>
<ol>
<li><b>Stall</b>: ง่ายที่สุด แต่ต้องหยุดหลาย cycle ("นักวิจัยบอกว่าไม่ค่อยดี")</li>
<li><b>Forwarding (Bypassing)</b>: สร้าง <b>เส้นทางพิเศษใน datapath</b> ส่งผลลัพธ์จากสถานะ Execute ของคำสั่ง add <b>กลับไปเป็น input</b> ของคำสั่งถัดไปเลย โดยไม่ต้องรอ write back</li>
<li><b>Code scheduling (จัดเรียงโค้ดใหม่)</b>: แก้ที่ <b>assembly หรือ compiler</b> เช่น หลัง load x2 แทนที่จะ add ทันที ให้เอาคำสั่งที่ไม่เกี่ยวข้อง (load x4) <b>มาทำคั่นก่อน</b> วิธีนี้ <b>ไม่ต้องเพิ่ม hardware (bus forward)</b> แต่ไปแก้ที่ compiler/assembler แทน</li>
</ol>""",
        },
        {
            "time": "≈18:40", "ch": None,
            "title": "Hazard ที่ 3: Control Hazard และ Branch Prediction",
            "slides": [("Chapter07", 14), ("Chapter07", 15), ("Chapter07", 17)],
            "body": """<ul>
<li>เกิดเมื่อ fetch คำสั่งถัดไปมาแล้ว แต่ <b>คำสั่งก่อนหน้าเป็น branch/jump</b> → กระโดดไปที่อื่น คำสั่งที่ fetch มา <b>ไม่ถูกใช้</b></li>
<li>วิธีแก้ที่ง่ายสุด: ใช้ <b>bubble / stall</b> จนกว่า pipeline จะกลับมาทำงานปกติ</li>
<li>แต่ stall ไปเรื่อย ๆ <b>เสียเวลา (waste)</b> จึงมีความพยายามออกแบบ <b>prediction</b>: ใช้ <b>สถิติ/probability</b> เดาว่า branch นี้จะกระโดดจริงไหม</li>
<li>ตัวอย่างของอาจารย์: <b>ลูป</b> ที่เช็กเงื่อนไขว่า i เท่ากับ 0 ไหม เมื่อยังลบไม่ถึง 0 ก็ <b>ไม่มีทางกระโดดออกจากลูป</b> จึง fetch คำสั่งถัดไปมาก่อนได้</li>
<li><b>แต่ prediction มีต้นทุนฮาร์ดแวร์สูง</b> ต้องออกแบบวงจรเก็บสถิติเพิ่มใน CPU อาจารย์บอกว่าส่วนใหญ่ <b>นิยมใช้วิธี stall มากกว่า</b> เพราะความซับซ้อนของวงจรทำ prediction มี cost สูงกว่าอยู่ดี</li>
</ul>""",
        },
        {
            "time": "≈20:00", "ch": None,
            "title": "สรุป Pipeline: 3 hazard และ Pipeline Registers",
            "slides": [("Chapter07", 18), ("Chapter07", 20)],
            "body": """<ul>
<li>สรุป: pipeline <b>ทำงานได้เร็ว</b> ปัญหาที่พบมี 3 type:
<ul>
<li><b>Structural hazard</b> – ใช้ resource ซ้ำกัน</li>
<li><b>Data hazard</b> – ข้อมูลยังไม่เสร็จ แต่ถูกเรียกใช้</li>
<li><b>Control hazard</b> – เกิด jump/branch ทำให้คำสั่งที่ fetch มาไม่ถูกใช้</li>
</ul></li>
<li>ทุก stage ของ datapath ต้องมี <b>pipeline registers</b> (ตัวสีฟ้าในรูป) เก็บข้อมูลจาก stage ก่อนหน้า ไม่งั้น <b>ข้อมูลจะถูกคำสั่งถัดไปทับทันที</b> เป็น hardware ที่เพิ่ม (ต้นทุน) แต่ทำให้ CPU ทำงานแบบ pipeline เร็วขึ้นได้</li>
</ul>""",
        },
        {
            "time": "≈24:20", "ch": "บทที่ 8: Parallel Processors",
            "title": "การจัดกลุ่มสถาปัตยกรรม (Flynn's Taxonomy): SISD / SIMD / MISD / MIMD",
            "slides": [("Chapter08", 9), ("Chapter01", 33)],
            "body": """<table>
<tr><th>ชนิด</th><th>ที่อาจารย์อธิบาย</th></tr>
<tr><td><b>SISD</b> (Single Instruction, Single Data)</td><td>CPU ปกติ (ต้นแบบดั้งเดิม)</td></tr>
<tr><td><b>SIMD</b> (Single Instruction, Multiple Data)</td><td>กลุ่ม <b>vector / array processor</b> ใช้คำนวณพวก <b>GPU</b> (เช่น พิกเซลของภาพเป็น vector/array ทำพร้อมกันทีเดียวหลาย ๆ อัน)</td></tr>
<tr><td><b>MISD</b> (Multiple Instruction, Single Data)</td><td><b>แทบไม่มี / ไม่มีเลยแล้ว</b></td></tr>
<tr><td><b>MIMD</b> (Multiple Instruction, Multiple Data)</td><td>แบ่ง 2 ค่าย: <b>Shared memory</b> (กลุ่ม <b>SMP</b> = symmetric multiprocessor ทุกตัวเท่า ๆ กัน เจอในเครื่อง PC / Intel ทั่วไป) กับ <b>Distributed memory</b> (แต่ละตัวมี memory ของตัวเอง = <b>cluster</b>)</td></tr>
</table>
<ul>
<li>กลุ่มที่ต้องการ high performance แบบมี <b>hardware/core จริง</b> (เช่น 8 core, 16 core) <b>≠</b> แบบ <b>แบ่งงานเป็น task</b> บน resource เดียว (เช่น VM ที่ซอย hardware ให้) ซึ่งไม่มี hardware จริงรองรับ</li>
<li><b>Multi-core</b> = ออกแบบ <b>duplicate</b> core ไปเลย ของใครของมัน</li>
</ul>""",
        },
        {
            "time": "≈28:00", "ch": None,
            "title": "Vector Processor และ Multithreading",
            "slides": [("Chapter08", 11), ("Chapter08", 16), ("Chapter08", 17)],
            "body": """<ul>
<li><b>Vector processor</b>: CPU บางประเภท เช่นตระกูล <b>RISC-V มี version ที่เป็น vector processor</b> มาผสม ส่วนใหญ่ใช้กับคำสั่งคำนวณคณิตศาสตร์เยอะ เช่น <b>คูณ-บวก-คูณ-บวก (multiply–accumulate)</b> ใน digital filter, vector ของภาพ, background subtraction, พีชคณิตเชิงเส้น (ตัวอย่างบนสไลด์: DAXPY)</li>
<li><b>Multithread</b>: ไม่ได้มี hardware เพิ่มจริง แต่ <b>ซอยคำสั่งออกเป็น thread</b> แล้วทำ <b>scheduling</b> processor ตาม thread — ไม่ต้องลงทุนเรื่อง CPU/hardware แต่ได้ลักษณะ parallel ได้เยอะ</li>
</ul>""",
        },
        {
            "time": "≈30:00", "ch": None,
            "title": "Shared Memory vs Distributed Memory",
            "slides": [("Chapter08", 19), ("Chapter08", 31)],
            "body": """<ul>
<li><b>Shared memory</b> (multiprocessor แบบ share): <b>ข้อดี</b> ไม่ต้อง duplicate memory ไปในแต่ละ core และ <b>ไม่ต้อง sync ข้อมูล</b> เมื่อใช้ข้อมูลก้อนเดียวกัน · <b>ข้อเสีย</b> ทุก core อ่าน/เขียนที่ memory ตัวเดียว ทำให้ <b>รุมกัน access</b> ยุ่งยาก</li>
<li><b>Distributed memory</b> (แต่ละ processor มี memory ของตัวเอง): update/sync ข้อมูลระหว่างกัน <b>ทำได้ยาก</b> ต้องมี <b>กระบวนการเพิ่มเติม</b></li>
</ul>""",
        },
        {
            "time": "≈31:30", "ch": None,
            "title": "GPU: SIMD, Fermi / Tesla และการใช้งาน AI",
            "slides": [("Chapter08", 23), ("Chapter08", 25)],
            "body": """<ul>
<li>GPU ตระกูล <b>Nvidia</b> เริ่มจากการ์ดธรรมดา/การ์ดเกม ทำ acceleration กราฟิกและการคำนวณคณิตศาสตร์</li>
<li>GPU แบบใหม่สำหรับ <b>AI</b>: มี CPU (Intel/AMD/Arm) เป็น control unit ใช้การคำนวณคณิตศาสตร์หนักมาก ตระกูล <b>DGX</b> ใช้ <b>train / สร้าง AI model</b> ราคาสูง</li>
<li>เมื่อได้ AI model แล้ว (เป็นสูตร/ตัวเลข) ตอน <b>execute</b> ใช้ <b>การ์ดเกมหรือการ์ดปกติ</b> ใน PC ก็ได้ ไม่จำเป็นต้องใช้ GPU ตัวใหญ่</li>
<li>หลักการ GPU = <b>SIMD</b>: คำสั่งชนิดเดียว (เช่นบวก/ลบ) ทำ <b>พร้อมกันทีเดียวกับข้อมูลจำนวนมาก</b> เช่นลบ <b>background</b> ของภาพก่อนทำ object detection (pixel เป็น array/vector)</li>
<li>บางค่ายออกแบบเป็น <b>vector-based</b> (สไลด์ตัวอย่าง <b>Nvidia Fermi</b>) ส่วน <b>Tesla</b> ใช้แบบ <b>multiprocessor</b> คือใช้หน่วย compute หลายหน่วยทำร่วมกันทีละเยอะ ๆ</li>
</ul>
<div class="box exam"><b>อาจารย์ปิดว่า:</b> "ท้ายสุด ก็น่าจะเป็นประมาณนี้ ที่อาจารย์จะออกในข้อสอบ"</div>""",
        },
        {
            "time": "≈35:00", "ch": "ช่วงท้ายคลิป: ถามตอบ",
            "title": "Q&A กับนักศึกษา",
            "slides": [("Chapter08", 23)],
            "body": """<ul>
<li><b>ถามเรื่องสไลด์หน้า 23</b> (รูป Graphics in the System): ตัวไหนใช้ train AI → <b>รูปด้านบน</b> ที่เป็น GPU + Intel CPU (ซ้าย) และแบบเดียวกันแต่เปลี่ยนเป็น AMD CPU (ขวา) ส่วนตอนเอาโมเดลมาใช้ → ใช้ <b>รูปล่างซ้าย</b> ซึ่งเหมือนการ์ดเกม/การ์ด VGA เสียบ slot PCI ปกติ</li>
<li><b>ข้อสอบเป็น multiple choice ทั้ง 60 ข้อไหม?</b> → อาจารย์ตอบ <b>"ใช่เลยครับ multiple choice"</b></li>
<li><b>CD กับ DVD ต่างกันอย่างไร</b> → ดูหัวข้อ "SSD vs HDD และสื่อเก็บข้อมูลอื่น ๆ" ด้านบน (sector ของ DVD เล็กกว่า ความหนาแน่นมากกว่า เก็บได้มากกว่า)</li>
</ul>
<p class="note">ภาพในคลิปช่วง 35:00–38:46 เป็นหน้าจอประชุม (ไม่มีสไลด์แล้ว) ข้อความของ Gemini ช่วงนี้ซ้ำกับเนื้อหาที่เคยถอดไปแล้ว ผมจึงไม่เพิ่มรายละเอียดอื่น</p>""",
        },
    ],
}
