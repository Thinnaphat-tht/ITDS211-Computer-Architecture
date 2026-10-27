"""ตรวจความสมดุลของตัวเลือก: เฉลยต้องไม่ยาว/สั้นเด่นกว่าตัวหลอก (build.py เรียกใช้กับชุดใน BALANCED)
python -X utf8 balance.py 1 2   → แสดงรายงานชุดที่ 1 และ 2
"""
import importlib.util, os, sys

MAX_RATIO = 1.4      # ตัวเลือกยาวสุด ÷ สั้นสุด (ข้ามเมื่อทุกตัวเลือกสั้น ≤ SHORT ตัวอักษร)
SHORT = 12
MAX_LONGEST = 9      # ต่อชุด 30 ข้อ: เฉลยเป็นตัวเลือกที่ยาวสุดตัวเดียวได้ไม่เกินกี่ข้อ (สุ่มปกติ ~7-8)


def check(qs, label="ชุด"):
    """คืน (ข้อผิดพลาด, สถิติ)"""
    errs, longest, shortest = [], 0, 0
    for i, q in enumerate(qs, 1):
        L = [len(x.strip()) for x in q["c"]]
        a = q["a"]
        if max(L) > SHORT and max(L) > MAX_RATIO * min(L):
            errs.append(f"{label} ข้อ {i}: ตัวเลือกยาว {min(L)}–{max(L)} ตัวอักษร (ยาวสุด/สั้นสุด = {max(L)/min(L):.2f} เกิน {MAX_RATIO})")
        if L[a] == max(L) and L.count(max(L)) == 1:
            longest += 1
        if L[a] == min(L) and L.count(min(L)) == 1:
            shortest += 1
    if longest > MAX_LONGEST:
        errs.append(f"{label}: เฉลยเป็นตัวเลือกที่ยาวสุดตัวเดียว {longest}/{len(qs)} ข้อ เกิน {MAX_LONGEST}")
    return errs, {"longest": longest, "shortest": shortest, "n": len(qs)}


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, here)
    for n in sys.argv[1:] or ["1", "2"]:
        spec = importlib.util.spec_from_file_location(f"quiz{n}", os.path.join(here, f"quiz{n}.py"))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        errs, st = check(m.SET, f"ชุด {n}")
        print(f"ชุด {n}: เฉลยยาวสุด {st['longest']}/{st['n']} · เฉลยสั้นสุด {st['shortest']}/{st['n']} · ปัญหา {len(errs)} จุด")
        for e in errs:
            print("  ", e)
