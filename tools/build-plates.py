"""Baut die Tafeln: lädt gemeinfreie Bilder und Editionsseiten, verkleinert sie und zeichnet die Übersichtskarte.

Schreibt assets/plates/<id>.jpg (höchstens 1600 px) und <id>_t.jpg (360 px breit). Die Quellen nennt data/plates.json.
Die Küstenlinien der Karte stammen aus Natural Earth (ne_50m_land, ne_50m_lakes; gemeinfrei) und werden beim Bauen geladen.
"""
import io
import json
import math
import time
import urllib.error
import urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "plates"
UA = {"User-Agent": "VitalienbruederSite/1.0 (research site; plates build)"}

SOURCES = {
    # Wikimedia Commons (gemeinfrei)
    "lubeca": ("https://upload.wikimedia.org/wikipedia/commons/9/9c/Nuremberg_chronicles_f_265-66_%28Lubeca%29.jpg", None),
    "elbing": ("https://upload.wikimedia.org/wikipedia/commons/0/0f/Siegel_Elbing_1350.jpg", None),
    "jungingen": ("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/AGAD_Pieczec_Konrada_von_Jungingen_wielkiego_mistrza_zakonu_krzyzackiego.png/1280px-AGAD_Pieczec_Konrada_von_Jungingen_wielkiego_mistrza_zakonu_krzyzackiego.png", None),
    "cartagotland": ("https://upload.wikimedia.org/wikipedia/commons/7/73/Carta_Marina_Gotland.jpeg", None),
    "stoewer": ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Hansa_ships_of_the_XIVth_and_XVth_centuries.jpg/1920px-Hansa_ships_of_the_XIVth_and_XVth_centuries.jpg", None),
    # Editionsseiten (Internet Archive)
    "hr168": ("https://archive.org/download/hanserecesse12roppgoog/page/n209_w1800.jpg", (0.02, 0.02, 0.98, 0.98)),
    "hr258": ("https://archive.org/download/hanserecesse12roppgoog/page/n299_w1800.jpg", (0.02, 0.02, 0.98, 0.98)),
    "hr304": ("https://archive.org/download/hanserecesse12roppgoog/page/n345_w1800.jpg", (0.02, 0.02, 0.98, 0.98)),
    "hr421": ("https://archive.org/download/hanserecesse12roppgoog/page/n462_w1800.jpg", (0.02, 0.02, 0.98, 0.98)),
    "hr491": ("https://archive.org/download/hanserecesse12roppgoog/page/n532_w1800.jpg", (0.02, 0.02, 0.98, 0.98)),
    "hr417": ("https://archive.org/download/hanserecesse12roppgoog/page/n458_w1800.jpg", (0.02, 0.02, 0.98, 0.98)),
    "srp217": ("https://archive.org/download/bub_gb_qtftAAAAIAAJ/page/n223_w1800.jpg", (0.04, 0.03, 0.97, 0.97)),
    "detmar50": ("https://archive.org/download/bub_gb_oqgKAAAAIAAJ/page/n76_w1800.jpg", (0.04, 0.02, 0.98, 0.98)),
}

NE = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/"


def fetch(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code != 429 or i == tries - 1:
                raise
            time.sleep(20 * (i + 1))


def save(im, pid):
    full = im.copy(); full.thumbnail((1600, 1600)); full.save(OUT / f"{pid}.jpg", quality=86)
    w = 360; t = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS); t.save(OUT / f"{pid}_t.jpg", quality=82)


PLACES = [  # (Name, Breite, Länge, Art) Art: s Stadt der Hanse, v Ort der Vitalienbrüder, x anderer Ort
    ("Lübeck", 53.87, 10.69, "s"), ("Hamburg", 53.55, 9.99, "s"), ("Stralsund", 54.31, 13.09, "s"),
    ("Wismar", 53.89, 11.47, "v"), ("Rostock", 54.09, 12.14, "v"),
    ("Danzig", 54.35, 18.65, "s"), ("Elbing", 54.16, 19.40, "s"), ("Thorn", 53.01, 18.60, "s"),
    ("Reval", 59.44, 24.75, "s"), ("Kampen", 52.56, 5.91, "s"),
    ("Stockholm", 59.33, 18.07, "v"), ("Visby", 57.64, 18.30, "v"), ("Bergen", 60.39, 5.32, "v"),
    ("Emden", 53.37, 7.21, "v"), ("Helgoland", 54.18, 7.89, "x"),
    ("Dragør", 55.59, 12.67, "x"), ("Skanör und Falsterbo", 55.40, 12.85, "x"), ("Lindholm", 55.50, 13.23, "x"),
    ("Bornholm", 55.13, 14.92, "x"), ("Falköping", 58.17, 13.55, "x"), ("Newa", 59.93, 30.25, "x"),
]

OFFS = {"Lübeck": (-95, -30), "Hamburg": (-20, 12), "Wismar": (-30, 14), "Rostock": (-40, -38), "Stralsund": (12, -30),
        "Dragør": (-90, -26), "Skanör und Falsterbo": (-250, 0), "Lindholm": (12, -12), "Danzig": (-78, -34),
        "Elbing": (12, -6), "Emden": (14, -12), "Helgoland": (-50, -36), "Kampen": (14, -16), "Newa": (-74, -30),
        "Visby": (14, -14), "Stockholm": (14, -18), "Bornholm": (14, -4)}


def draw_map():
    lon0, lon1, lat0, lat1 = 3.5, 31.5, 52.2, 61.2
    k = math.cos(math.radians(56.5))
    W = 1500; H = round(W * (lat1 - lat0) / ((lon1 - lon0) * k)) + 120
    X = lambda lon: 40 + (lon - lon0) / (lon1 - lon0) * (W - 80)
    Y = lambda lat: 90 + (lat1 - lat) / (lat1 - lat0) * (H - 170)
    sea, land, lake = (214, 226, 230), (240, 233, 219), (214, 226, 230)
    im = Image.new("RGB", (W, H), sea); d = ImageDraw.Draw(im)

    def polys(gj):
        for f in gj["features"]:
            g = f["geometry"]
            for poly in (g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]):
                ring = poly[0]
                if any(lon0 - 4 < p[0] < lon1 + 4 and lat0 - 3 < p[1] < lat1 + 3 for p in ring):
                    yield [(X(p[0]), Y(p[1])) for p in ring]

    for r in polys(json.loads(fetch(NE + "ne_50m_land.geojson"))):
        d.polygon(r, fill=land, outline=(150, 135, 110))
    for r in polys(json.loads(fetch(NE + "ne_50m_lakes.geojson"))):
        d.polygon(r, fill=lake, outline=(150, 135, 110))

    try:
        f = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 22); fb = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 30); fs = ImageFont.truetype("C:/Windows/Fonts/georgiai.ttf", 19)
    except OSError:
        f = fb = fs = ImageFont.load_default()
    d.rectangle([0, 0, W, 70], fill=(250, 246, 238)); d.rectangle([0, H - 64, W, H], fill=(250, 246, 238))
    d.rectangle([12, 12, W - 12, H - 12], outline=(107, 63, 29), width=3)
    d.text((32, 22), "Die Vitalienbrüder und die Hanse, 1389–1401: Orte in den Texten", font=fb, fill=(107, 63, 29))
    ly = H - 48
    d.text((32, ly), "Schematisch: Küsten nach Natural Earth, Orte nach heutigen Koordinaten; keine Grenzen.", font=fs, fill=(98, 88, 95))
    lx = 870
    d.ellipse([lx, ly + 4, lx + 14, ly + 18], outline=(35, 28, 34), width=3); d.text((lx + 22, ly), "Hansestadt", font=fs, fill=(98, 88, 95))
    d.ellipse([lx + 150, ly + 4, lx + 164, ly + 18], fill=(140, 28, 43)); d.text((lx + 172, ly), "Ort der Vitalienbrüder", font=fs, fill=(98, 88, 95))
    d.ellipse([lx + 400, ly + 7, lx + 408, ly + 15], fill=(35, 28, 34)); d.text((lx + 416, ly), "anderer Ort", font=fs, fill=(98, 88, 95))
    for name, la, lo, kind in PLACES:
        x, y = X(lo), Y(la)
        if kind == "v":
            d.ellipse([x - 8, y - 8, x + 8, y + 8], fill=(140, 28, 43))
        elif kind == "s":
            d.ellipse([x - 7, y - 7, x + 7, y + 7], outline=(35, 28, 34), width=3)
        else:
            d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(35, 28, 34))
        dx, dy = OFFS.get(name, (12, -14))
        d.text((x + dx, y + dy), name, font=f, fill=(35, 28, 34))
    for txt, lo, la in [("OSTSEE", 17.0, 56.2), ("NORDSEE", 4.6, 56.6), ("SCHWEDEN", 14.6, 59.6), ("NORWEGEN", 7.6, 61.0),
                        ("DÄNEMARK", 8.6, 56.2), ("GOTLAND", 18.9, 57.2), ("PREUSSEN", 20.6, 53.7), ("LIVLAND", 25.2, 57.9),
                        ("MECKLENBURG", 11.6, 53.3)]:
        d.text((X(lo), Y(la)), txt, font=fs, fill=(98, 88, 95))
    return im


def main(only=None):
    """Ohne Argumente alles bauen; mit Kennungen (z. B. hr417 karte) nur diese."""
    OUT.mkdir(parents=True, exist_ok=True)
    for pid, (url, crop) in SOURCES.items():
        if only and pid not in only:
            continue
        im = Image.open(io.BytesIO(fetch(url))).convert("RGB")
        if crop:
            w, h = im.size
            im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
        save(im, pid); print(pid, im.size)
    if not only or "karte" in only:
        save(draw_map(), "karte"); print("karte")


if __name__ == "__main__":
    import sys
    main(set(sys.argv[1:]) or None)
