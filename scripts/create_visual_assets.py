from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

OUT = Path("assets/security-study-map.png")
OUT.parent.mkdir(exist_ok=True)

W, H = 1400, 720
img = Image.new("RGB", (W, H), "#f7fafc")
draw = ImageDraw.Draw(img)


def font(size: int, bold: bool = False):
    candidates = [
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


title = font(58, True)
heading = font(30, True)
body = font(21)
small = font(19)

draw.rectangle((0, 0, W, H), fill="#f7fafc")
draw.rectangle((0, 0, W, 140), fill="#103849")
draw.text((70, 42), "Software Security Study Map", font=title, fill="#ffffff")
draw.text((74, 112), "Risk, secure development, input, code review, access, errors, and authentication", font=small, fill="#c8e8f2")

colors = ["#2f9e8f", "#d86f45", "#4169a8", "#7a5ca5", "#d0a536", "#497f55", "#b44d64", "#4c7b9c"]
cards = [
    ("01", "Security Basics", "CIA, risk, defects, bugs, flaws, vulnerabilities"),
    ("02", "Secure SDLC", "SAMM, ISO 27034, OWASP Top 10, CWE"),
    ("03", "Handling Input", "Trusted vs untrusted input, validation, SQL injection"),
    ("04", "Static Analysis", "SAST tools, data flow, control flow, AST rules"),
    ("05", "Buffer Overflow", "Memory overrun, stack impact, compiler defenses"),
    ("06", "Access Control", "Vertical, horizontal, context checks, IDOR/BOLA"),
    ("07", "Errors", "Return codes, exceptions, leaks, logging, debugging"),
    ("08", "Authentication", "Sessions, credentials, MFA, password controls"),
]

x0, y0 = 70, 190
card_w, card_h = 305, 190
gap_x, gap_y = 35, 38
for i, (num, label, desc) in enumerate(cards):
    row, col = divmod(i, 4)
    x = x0 + col * (card_w + gap_x)
    y = y0 + row * (card_h + gap_y)
    c = colors[i]
    draw.rounded_rectangle((x, y, x + card_w, y + card_h), radius=18, fill="#ffffff", outline="#d6e2ea", width=2)
    draw.ellipse((x + 22, y + 22, x + 78, y + 78), fill=c)
    draw.text((x + 40, y + 36), num, font=small, fill="#ffffff", anchor="mm")
    draw.text((x + 94, y + 27), label, font=heading, fill="#15313d")
    draw.line((x + 24, y + 96, x + card_w - 24, y + 96), fill="#e4edf2", width=2)
    wrapped = "\n".join(textwrap.wrap(desc, width=24))
    draw.multiline_text((x + 24, y + 114), wrapped, font=body, fill="#365461", spacing=5)

draw.rounded_rectangle((70, 650, W - 70, 694), radius=22, fill="#e8f4f0")
draw.text((92, 670), "Memory anchors: CIA, RTK pillars, UISDF risk loop, STRIDE, DREAD, SAFE input, SHIELD access, FCL logs.", font=small, fill="#24483e", anchor="lm")

img.save(OUT)
print(OUT)
