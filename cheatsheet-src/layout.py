"""จัดวางบล็อกลงหน้า/คอลัมน์ (ชื่อบล็อก = ไฟล์ parts/blocks/<ชื่อ>.html)"""
PAGES = [
    dict(title="ITDS211 · หน้า 1/4 · Ch01–03 Basic · Bus · Interrupt · Data Rep",
         cols=[["ch01_basic", "ch01_extra", "ch01_perf", "ch02_model"], ["ch02_regs", "ch02_int", "ch03_data"]]),
    dict(title="ITDS211 · หน้า 2/4 · Ch03 Assembly · Ch04 Memory &amp; Cache",
         cols=[["ch03_asm", "ch04_hier"], ["ch04_cache", "ch04_write", "ch04_assoc", "ch04_amat"]]),
    dict(title="ITDS211 · หน้า 3/4 · Ch05 I/O · Ch06 Storage",
         cols=[["ch05_io", "ch05_dev", "ch05_std"], ["ch06_hdd", "ch06_more", "ch06_raid", "ch06_ssd"]]),
    dict(title="ITDS211 · หน้า 4/4 · Ch07 Pipeline · Ch08 Parallel · สูตร · เช็กข้อหลอก",
         cols=[["ch07_pipe", "formulas"], ["ch08_par", "ch08_gpu", "ch04_end"]], full=["traps"]),
]
