from pathlib import Path
import sys
from pypdf import PdfReader

pdf = Path(sys.argv[1])
page_number = int(sys.argv[2])
out_dir = Path(sys.argv[3])
out_dir.mkdir(parents=True, exist_ok=True)

page = PdfReader(str(pdf)).pages[page_number - 1]
for index, image in enumerate(page.images, start=1):
    suffix = Path(image.name).suffix or ".bin"
    out_path = out_dir / f"page_{page_number:03}_{index:02}{suffix}"
    out_path.write_bytes(image.data)
    print(out_path)
