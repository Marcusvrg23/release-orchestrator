from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1280, 640
BG = (11, 15, 22)
PANEL = (20, 27, 38)
TEXT = (239, 244, 250)
MUTED = (150, 163, 184)
ACCENT = (72, 214, 205)
ACCENT2 = (129, 140, 248)
GOOD = (74, 222, 128)

def font(size, bold=False):
    candidates = [
        Path(r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf"),
        Path(r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()

def rounded(draw, box, radius=24, fill=PANEL, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def center_text(draw, xy, text, f, fill=TEXT):
    box = draw.textbbox((0, 0), text, font=f)
    x = xy[0] - (box[2] - box[0]) / 2
    y = xy[1] - (box[3] - box[1]) / 2
    draw.text((x, y), text, font=f, fill=fill)
def social_preview():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((48, 48, W-48, H-48), radius=32, outline=(44, 56, 74), width=2)
    d.text((88, 90), "RELEASE ORCHESTRATOR", font=font(26, True), fill=ACCENT)
    d.text((88, 145), "Ship with evidence,", font=font(64, True), fill=TEXT)
    d.text((88, 220), "not agent confidence.", font=font(64, True), fill=TEXT)
    d.text((90, 320), "The orchestration protocol that decides", font=font(30), fill=MUTED)
    d.text((90, 360), "when NOT to use another agent.", font=font(30, True), fill=ACCENT2)

    x0, y0 = 92, 470
    labels = ["ROOT", "GATE", "SPECIALIST", "EVIDENCE", "VERIFY"]
    widths = [120, 120, 190, 155, 135]
    x = x0
    for idx, (label, bw) in enumerate(zip(labels, widths)):
        rounded(d, (x, y0, x+bw, y0+58), radius=16, fill=PANEL, outline=ACCENT if idx in (1,3,4) else (55,67,84), width=2)
        center_text(d, (x+bw/2, y0+29), label, font(20, True), ACCENT if idx in (1,3,4) else TEXT)
        x += bw
        if idx < len(labels)-1:
            d.line((x+8, y0+29, x+40, y0+29), fill=MUTED, width=3)
            d.polygon([(x+40,y0+29),(x+30,y0+23),(x+30,y0+35)], fill=MUTED)
            x += 54

    d.text((90, 574), "github.com/Marcusvrg23/release-orchestrator", font=font(20), fill=MUTED)
    im.save(OUT / "social-preview.png", optimize=True)
def demo_frame(step):
    im = Image.new("RGB", (1200, 675), BG)
    d = ImageDraw.Draw(im)
    d.text((56, 42), "Release Orchestrator", font=font(34, True), fill=TEXT)
    d.text((56, 88), "Delegation must earn its cost.", font=font(24), fill=ACCENT)

    stages = [
        ("ROOT", "Own the task"),
        ("DELEGATION GATE", "Is a specialist materially useful?"),
        ("SPECIALIST", "Bounded, read-only by default"),
        ("EVIDENCE", "Return findings, not authority"),
        ("ROOT VERIFY", "Check the authoritative surface"),
        ("DECIDE", "Release claim only with evidence"),
    ]
    y = 160
    for i, (title, sub) in enumerate(stages):
        active = i <= step
        outline = ACCENT if active else (50, 60, 76)
        fill = (17, 31, 39) if active else PANEL
        rounded(d, (90, y, 1110, y+68), radius=18, fill=fill, outline=outline, width=2)
        d.text((120, y+14), title, font=font(22, True), fill=TEXT if active else MUTED)
        d.text((390, y+17), sub, font=font(20), fill=ACCENT if active else MUTED)
        if i < len(stages)-1:
            d.line((600, y+68, 600, y+88), fill=ACCENT if active else (50,60,76), width=3)
            d.polygon([(600,y+90),(593,y+80),(607,y+80)], fill=ACCENT if active else (50,60,76))
        y += 86

    footer = "UNDERSTAND → REPRODUCE → ISOLATE → CHANGE → VERIFY → PRESERVE → DECIDE"
    center_text(d, (600, 640), footer, font(17, True), GOOD if step == len(stages)-1 else MUTED)
    return im

def demo_gif():
    frames = [demo_frame(i) for i in range(6)]
    durations = [750, 850, 850, 850, 900, 1700]
    frames[0].save(
        OUT / "release-orchestrator-demo.gif",
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=True,
    )

if __name__ == "__main__":
    social_preview()
    demo_gif()
    print(OUT / "social-preview.png")
    print(OUT / "release-orchestrator-demo.gif")
