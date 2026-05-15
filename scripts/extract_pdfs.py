from pathlib import Path
from pypdf import PdfReader

SLIDE_DIR = Path(r"C:\Users\ihsan\OneDrive - Universiti Tenaga Nasional\trimester 2 2526\SOFTSEC CCSB5113\SLIDE")
OUT_DIR = Path("extracted")

PDFS = [
    "Chapter 1_Overview of Software Security.pdf",
    "Chapter 2_Secure SDLC.pdf",
    "Chapter 3_Handling Input.pdf",
    "Chapter 4_Static Analysis Framework.pdf",
    "Chapter 5_Buffer Overflow.pdf",
    "Chapter 6_Web Application_Broken Access Control.pdf",
    "Chapter 7_Error and Exception.pdf",
    "Chapter 8_Broken Authentication.pdf",
]


def clean_text(text: str) -> str:
    lines = []
    for raw in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        line = " ".join(raw.split())
        if line:
            lines.append(line)
    return "\n".join(lines)


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    summary_lines = []
    for pdf_name in PDFS:
        path = SLIDE_DIR / pdf_name
        reader = PdfReader(str(path))
        chapter_stem = pdf_name.removesuffix(".pdf")
        chapter_dir = OUT_DIR / chapter_stem
        chapter_dir.mkdir(exist_ok=True)

        combined = []
        for page_index, page in enumerate(reader.pages, start=1):
            text = clean_text(page.extract_text() or "")
            combined.append(f"--- Page {page_index} ---\n{text}\n")
            (chapter_dir / f"page_{page_index:03}.txt").write_text(text, encoding="utf-8")

        (OUT_DIR / f"{chapter_stem}.txt").write_text("\n".join(combined), encoding="utf-8")
        summary_lines.append(f"{chapter_stem}: {len(reader.pages)} pages")

    (OUT_DIR / "summary.txt").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
