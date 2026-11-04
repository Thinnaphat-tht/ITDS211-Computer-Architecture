"""จัดวางบล็อกลงหน้า/คอลัมน์ ตามลำดับบท Ch01 -> Ch08 (ชื่อบล็อก = ไฟล์ parts/blocks/<ชื่อ>.html)"""
PAGES = [
    dict(cls="p1", title="หน้า 1/4 · Ch01 พื้นฐาน · Performance · Ch02 Bus · Interrupt",
         top=["idx"],
         cols=[["p1_flow", "p1_perf", "p1_model"], ["p4_bus", "p1_int"]]),
    dict(cls="p2", title="หน้า 2/4 · Ch03 Data Representation · Assembly",
         cols=[["p1_data"], ["p2_asm", "p1_endian"]]),
    dict(cls="p3", title="หน้า 3/4 · Ch04 Memory &amp; Cache",
         cols=[["p3_hier", "p3_assoc"], ["p3_direct", "p3_calc"]]),
    dict(cls="p4", title="หน้า 4/4 · Ch05 I/O · Ch06 Storage · Ch07 Pipeline · Ch08 Parallel",
         cols=[["p4_io", "p4_storage"], ["p7_a", "p7_b", "p4_par"]], full=["p2_qa"]),
]
