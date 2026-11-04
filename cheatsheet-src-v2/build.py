"""สร้าง ITDS211-Cheatsheet-v2.pdf จาก cheatsheet.html (Edge headless)
รัน: python -X utf8 build.py   (ต้องมี pymupdf และ Microsoft Edge)
ขั้นตอน: 1) dump-dom อ่านรายงานความพอดีของแต่ละคอลัมน์  2) print-to-pdf  3) นับหน้า + เรนเดอร์ PNG ตัวอย่าง
"""
import json, os, re, subprocess, sys, tempfile
import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(HERE, "cheatsheet.html")  # สร้างอัตโนมัติจาก parts/head + blocks (ตาม layout.py) + tail — ห้ามแก้ไฟล์นี้ตรง ๆ
PARTS = os.path.join(HERE, "parts")
sys.path.insert(0, HERE)
from layout import PAGES
LEGEND = '<b class="s">★</b> อาจารย์เน้น · <b style="color:var(--red)">⚠</b> ข้อหลอก · <span class="x">เทา</span> = เสริมจากสไลด์'
_read = lambda n: open(os.path.join(PARTS, n), encoding="utf-8").read()
_blk = lambda n: _read(f"blocks/{n}.html").strip()


def _page(pg):
    cols = "".join('<div class="col">' + chr(10) + (chr(10) * 2).join(_blk(n) for n in col) + chr(10) + '</div>' + chr(10) for col in pg["cols"])
    full = chr(10).join(_blk(n) for n in pg.get("full", []))
    top = chr(10).join(_blk(n) for n in pg.get("top", []))
    return ('<section class="page ' + pg["cls"] + '"><div class="ph"><b>' + pg["title"] + '</b><span>' + LEGEND + '</span></div>' + top +
            '<div class="cols">' + cols + '</div>' + full + '</section>' + chr(10))


with open(SRC, "w", encoding="utf-8") as _f:
    _f.write(_read("head.html") + "".join(_page(p) for p in PAGES) + _read("tail.html"))
PDF = os.path.join(ROOT, "ITDS211-Cheatsheet-v2.pdf")
PREVIEW = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "preview")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
URL = "file:///" + SRC.replace("\\", "/").replace(" ", "%20")
PROFILE = tempfile.mkdtemp(prefix="cs-edge-")  # โปรไฟล์แยกต่อรอบ กัน Edge ค้างจากรอบก่อน
FLAGS = ["--headless", "--disable-gpu", "--virtual-time-budget=6000", f"--user-data-dir={PROFILE}"]


def kill_leftover():
    """ปิดเฉพาะ Edge headless ของรอบนี้ (ไม่แตะ Edge ปกติของผู้ใช้)"""
    key = os.path.basename(PROFILE)
    subprocess.run(["powershell", "-NoProfile", "-Command",
                    f"Get-CimInstance Win32_Process -Filter \"Name='msedge.exe'\" | Where-Object {{ $_.CommandLine -like '*{key}*' }} | ForEach-Object {{ Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }}"],
                   capture_output=True)


def run(extra, capture=False):
    for attempt in (1, 2, 3):  # Edge headless สุ่มค้างบางครั้ง → ลองใหม่
        try:
            return subprocess.run([EDGE, *FLAGS, *extra, URL], capture_output=capture, timeout=40,
                                  encoding="utf-8" if capture else None, errors="replace" if capture else None)
        except subprocess.TimeoutExpired:
            print(f"  (Edge ค้าง ลองใหม่ครั้งที่ {attempt})")
        finally:
            kill_leftover()
    sys.exit("Edge ค้างเกินกำหนด")


# 1) รายงานความพอดี
dom = run(["--dump-dom"], capture=True).stdout
m = re.search(r'<pre id="fit"[^>]*>(.*?)</pre>', dom, re.S)
if not m or not m.group(1).strip():
    sys.exit("ไม่พบรายงานความพอดี (fit) ใน DOM")
fit = json.loads(m.group(1).replace("&quot;", '"').replace("&amp;", "&"))
bad = False
print("line-height ต่อหน้า:", fit.get("lhs"))
print("หน้า/คอลัมน์   ใช้ไป(mm)  ที่มี(mm)  เหลือ(mm)")
for r in fit["cols"]:
    left = r["avail"] - r["need"]
    flag = "  <<< ล้น" if r["over"] or left < -0.3 else ""
    bad |= bool(flag)
    print(f'  p{r["p"]} c{r["c"]}      {r["need"]:7.1f}   {r["avail"]:7.1f}   {left:7.1f}{flag}')
if os.environ.get("SECS"):
    for s_ in fit["secs"]:
        print(f'    p{s_["p"]}c{s_["c"]} {s_["h"]:6.1f}  {s_["t"]}')
for w in fit["wide"]:
    bad = True
    print("  กว้างล้น:", w)

# 2) PDF
if os.path.exists(PDF):
    os.remove(PDF)
run(["--no-pdf-header-footer", f"--print-to-pdf={PDF}"])
if not os.path.exists(PDF):
    sys.exit("สร้าง PDF ไม่สำเร็จ")

# 3) ตรวจหน้า + พรีวิว
d = fitz.open(PDF)
print("PDF:", PDF, "| หน้า:", len(d), "| ขนาดหน้า:", [tuple(round(x) for x in (p.rect.width, p.rect.height)) for p in d][:1], "(pt; A4=595x842)")
os.makedirs(PREVIEW, exist_ok=True)
for i, p in enumerate(d, 1):
    p.get_pixmap(matrix=fitz.Matrix(1.9, 1.9)).save(os.path.join(PREVIEW, f"p{i}.png"))
print("พรีวิว:", PREVIEW)
if len(d) != 4:
    print("!!! ต้องได้ 4 หน้าพอดี แต่ได้", len(d))
    bad = True
sys.exit(1 if bad else 0)
