# คลิปที่ 3: 2026-10-25 19-16-59 (11:32) บทที่ 5 I/O
CLIP = {
    "id": "v3",
    "file": "2026-10-25 19-16-59",
    "dur": "11:32",
    "title": "บทที่ 5 I/O Systems",
    "scope": "Ch05 I/O Module · เทคนิค 3 แบบ · Interrupt-driven I/O · การระบุอุปกรณ์ (Device Identification)",
    "intro": """<p>คลิปสั้น เริ่มต้นหลังพักเบรก อาจารย์เข้าสู่บทที่ 5 (I/O) ซึ่งเรียกว่า "ก้อนใหญ่ๆ"</p>
<p class="note">ซับของคลิปนี้มีถึง 10:58 จากความยาว 11:32 และตอนท้ายถอดเสียงไม่ครบ (อาจารย์กำลังเล่าเรื่องการเลือกอุปกรณ์ด้วยวงจรประเภท multiplexer) อาจารย์ไม่ได้พูดคำว่า "เน้นออกสอบ" ตรง ๆ ในคลิปนี้</p>""",
    "sections": [
        {
            "time": "00:33", "ch": "บทที่ 5: ระบบ I/O",
            "title": "I/O และ External Device",
            "slides": [("Chapter05", 5)],
            "body": """<ul>
<li>I/O = Input / Output ใช้ <b>buffer</b> เก็บข้อมูลที่ผ่านเข้า-ออก</li>
<li>ข้อมูลอาจเป็น <b>digital</b> หรือ <b>analog</b> ขึ้นกับว่าส่งผ่านทางสายหรืออากาศ (ในแผนภาพคือ <b>Transducer</b> ที่แปลงสัญญาณ)</li>
<li>ในสไลด์ External Device ประกอบด้วย Control Logic, Buffer, Transducer มีเส้น Control, Status, Data</li>
</ul>""",
        },
        {
            "time": "01:04", "ch": None,
            "title": "หน้าที่หลักของ I/O Module (5 ข้อ)",
            "slides": [("Chapter05", 6)],
            "body": """<ol>
<li><b>Control &amp; timing</b>: ควบคุมการไหลของข้อมูลระหว่างภายในกับอุปกรณ์ภายนอก</li>
<li><b>Processor communication</b>: ถอดรหัส command, ส่งข้อมูล, รายงาน status, จดจำ <b>address</b> ปลายทาง</li>
<li><b>Device communication</b>: คุยกับอุปกรณ์ด้วย command</li>
<li><b>Data buffering</b>: เก็บข้อมูลที่ส่งเข้ามาไว้ก่อน (ถ้า input ก็เอาเข้า memory ถ้า output ก็ส่งออกไปอุปกรณ์)</li>
<li><b>Error detection</b>: ตรวจจับ error ที่เกิดขึ้นระหว่างส่งผ่าน I/O</li>
</ol>
<div class="box key"><b>ทำไมต้องมี buffer:</b> ความเร็วของ memory เร็วมาก แต่ I/O ช้ากว่ามาก buffer ช่วย <b>balance speed</b> เวลา processing ของ memory ตามไม่ทัน</div>""",
        },
        {
            "time": "02:38", "ch": None,
            "title": "ไดอะแกรมของ I/O Module",
            "slides": [("Chapter05", 7)],
            "body": """<ul>
<li><b>Address lines</b>: บอกว่าจะคุยกับ I/O ตัวไหน</li>
<li><b>Control lines</b>: บอกว่า I/O ต้องทำอะไร</li>
<li><b>Data lines / data bus</b>: ชุดข้อมูลที่ส่งผ่าน</li>
<li>กลุ่ม <b>Status</b> และ control ต่าง ๆ ที่เกี่ยวข้อง</li>
</ul>""",
        },
        {
            "time": "03:40", "ch": None,
            "title": "เทคนิคการทำ I/O 3 แบบ",
            "slides": [("Chapter05", 8), ("Chapter05", 9), ("Chapter05", 11)],
            "body": """<ol>
<li><b>Programmed I/O</b> (ง่ายที่สุด): processor <b>ยิงคำสั่ง</b>ไปให้ I/O แล้ว <b>รอ</b>จนกว่า I/O ตอบกลับ จึงได้ข้อมูล คำสั่งไม่ยาก แต่ <b>เสียเวลา processor</b> เพราะต้องนั่งรอ (ไม่มี interrupt)</li>
<li><b>Interrupt-driven I/O</b>: processor สั่งแล้ว <b>ไปทำงานอื่นต่อได้</b> เมื่อ I/O พร้อมส่งข้อมูลจึง <b>interrupt</b> กลับมา แล้ว processor ค่อยหันมารับ/ส่งข้อมูล</li>
<li><b>DMA (Direct Memory Access)</b>: <b>I/O กับ main memory แลกเปลี่ยนข้อมูลกันตรง ๆ</b> โดย CPU ไม่ต้องยุ่ง CPU ไปคำนวณงานของตัวเอง</li>
</ol>
<div class="box key"><b>อาจารย์บอกว่า DMA เป็นแบบที่ "นิยมใช้ใน architecture ปัจจุบันมาก"</b> ส่วน flow ฝั่ง CPU ก็ง่ายกว่ากันเยอะ เพราะ CPU ปล่อยให้ตัว DMA จัดการกับ I/O</div>""",
        },
        {
            "time": "06:13", "ch": None,
            "title": "I/O Commands และ Flowchart ของแต่ละเทคนิค",
            "slides": [("Chapter05", 10), ("Chapter05", 11)],
            "body": """<ul>
<li>คำสั่ง (command) ของ I/O มี 4 แบบ: <b>Control</b> (บอกให้ทำอะไร), <b>Test</b> (ดู status ก่อน), <b>Read</b>, <b>Write</b> (I/O มีทั้ง input และ output)</li>
<li>แบบ <b>Programmed</b>: flowchart เรียงเป็น sequence ไม่ยาก</li>
<li>แบบ <b>Interrupt</b>: processor แยกออกมาทำงานของตัวเองได้ และทำงานกับ I/O ก็ต่อเมื่อถูก interrupt</li>
<li>แบบ <b>DMA</b>: flow ของ CPU ง่ายสุด เพราะแยกออกจากกัน</li>
</ul>""",
        },
        {
            "time": "07:14", "ch": None,
            "title": "Interrupt-driven I/O: สิ่งที่เกิดเมื่อมี Interrupt",
            "slides": [("Chapter05", 17)],
            "body": """<ul>
<li>ทุกครั้งที่เกิด interrupt ต้อง <b>เก็บค่า PC</b> และ <b>status register</b> ไว้ก่อนเริ่มทำงาน (เหมือน flow ที่เคยเรียนใน Ch02)</li>
<li>จากนั้น <b>PC ถูกเปลี่ยนเป็นค่าเริ่มต้นของ ISR</b> แล้วเข้าไปรัน</li>
<li>เมื่อรัน interrupt เสร็จ <b>return</b>: เอาค่า PC เดิมก่อนกระโดดกลับเข้า PC และ <b>คืนค่าใน stack ทั้งหมด</b> แล้วจึงกลับมาทำงานต่อ</li>
</ul>""",
        },
        {
            "time": "08:48", "ch": None,
            "title": "Device Identification: ระบุว่าใครเป็นคนส่ง Interrupt (4 แบบ)",
            "slides": [("Chapter05", 19)],
            "body": """<ol>
<li><b>Multiple interrupt lines</b>: แยกเส้น interrupt คนละเส้น ตรงไปตรงมา ทำให้รู้ทันทีว่าใครเรียก <b>ข้อเสีย</b>: ถ้ามี I/O เยอะ เส้น interrupt ก็เยอะตาม</li>
<li><b>Software poll</b>: processor กระโดดไปที่ routine ที่ไล่ถาม (poll) ทีละ I/O module ว่าใครเป็นคนเรียก (ใช้เวลานาน)</li>
<li><b>Daisy chain</b> (hardware poll, vectored): กำหนด <b>priority</b> ว่าใครสำคัญสูง/ต่ำ ส่งสัญญาณ interrupt acknowledge ต่อกันเป็นลูกโซ่</li>
<li><b>Bus arbitration</b> (vectored): I/O module ต้อง <b>ขอสิทธิ์คุม bus ก่อน</b> จึงจะขอ interrupt ได้ เมื่อได้รับ request แล้ว module จะส่ง <b>address/vector ของ device</b> ผ่านสาย data/address</li>
</ol>
<p class="note">ตอนท้ายคลิป (ประมาณ 10:24–10:58) อาจารย์พูดถึงเทคนิคการต่อพ่วงกับ I/O ที่คล้ายวงจรประเภท <b>multiplexer</b> (เลือก 1 จาก 8) ซับถอดได้ไม่ครบ จึงไม่สรุปรายละเอียด</p>""",
        },
    ],
}
