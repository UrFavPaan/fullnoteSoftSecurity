from pathlib import Path
import sys
from pdf2image import convert_from_path

pdf = Path(sys.argv[1])
page = int(sys.argv[2])
out = Path(sys.argv[3])
out.parent.mkdir(exist_ok=True)
images = convert_from_path(str(pdf), first_page=page, last_page=page, dpi=140)
images[0].save(out)
