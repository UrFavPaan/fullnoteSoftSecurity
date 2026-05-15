from pathlib import Path

OUT_DIR = Path("extracted")


def split_pages(text: str) -> list[tuple[int, str]]:
    pages = []
    for chunk in text.split("--- Page "):
        chunk = chunk.strip()
        if not chunk:
            continue
        page_no_text, _, body = chunk.partition(" ---")
        try:
            page_no = int(page_no_text.strip())
        except ValueError:
            continue
        pages.append((page_no, body.strip()))
    return pages


def title_for(body: str) -> str:
    skip = {
        "By:",
        ".com",
        "presentationgo.com",
        "Â© presentationgo.com",
        "© presentationgo.com",
    }
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    meaningful = [line for line in lines if line not in skip and not line.isdigit()]
    return meaningful[0] if meaningful else "(blank)"


def main() -> None:
    lines = []
    for path in sorted(OUT_DIR.glob("Chapter *.txt")):
        lines.append(f"# {path.stem}")
        for page_no, body in split_pages(path.read_text(encoding="utf-8")):
            lines.append(f"{page_no:03}: {title_for(body)}")
        lines.append("")
    Path("extracted/page_titles.txt").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
