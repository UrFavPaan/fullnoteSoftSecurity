from pathlib import Path

for path in sorted(Path("extracted").glob("Chapter *.txt")):
    print(f"# {path.stem}")
    text = path.read_text(encoding="utf-8")
    for chunk in text.split("--- Page "):
        chunk = chunk.strip()
        if not chunk:
            continue
        page_no_text, _, body = chunk.partition(" ---")
        body = body.strip()
        try:
            page_no = int(page_no_text.strip())
        except ValueError:
            continue
        useful_lines = [
            line.strip()
            for line in body.splitlines()
            if line.strip()
            and line.strip()
            not in {"By:", ".com", "presentationgo.com", "Â© presentationgo.com"}
            and not line.strip().isdigit()
        ]
        print(f"{page_no:03}: chars={sum(len(x) for x in useful_lines):4} lines={len(useful_lines):2} title={useful_lines[0] if useful_lines else '(blank)'}")
    print()
