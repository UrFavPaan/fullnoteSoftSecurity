from pathlib import Path
import json

REPLACEMENTS = {
    "â€”": "-",
    "â€“": "-",
    "â€™": "'",
    "â€˜": "'",
    "â€œ": '"',
    "â€": '"',
    "â€¢": "-",
    "âœ“": "",
    "â–ª": "-",
    "Â©": "(c)",
}


def clean(value: str) -> str:
    for bad, good in REPLACEMENTS.items():
        value = value.replace(bad, good)
    return " ".join(value.split())

lines = Path("extracted/page_titles.txt").read_text(encoding="utf-8").splitlines()
coverage = []
current = None
for line in lines:
    if not line.strip():
        continue
    if line.startswith("# "):
        current = {"chapter": clean(line[2:].strip()), "slides": []}
        coverage.append(current)
        continue
    if current and ":" in line:
        page, title = line.split(":", 1)
        current["slides"].append({"page": int(page), "title": clean(title.strip())})

Path("coverage.js").write_text(
    "const COVERAGE = " + json.dumps(coverage, indent=2) + ";\n",
    encoding="utf-8",
)
print("coverage.js")
