"""Builds the single-file page: python3 -I build.py  ->  ../cre8-landing/index.html"""
import base64, json, pathlib
here = pathlib.Path(__file__).resolve().parent
html = (here / "index.html").read_text(encoding="utf-8")
imgs = {p.stem: "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode() for p in sorted((here / "images").glob("*.jpg"))}
marker = "const IMG = {};"
assert marker in html, "IMG marker missing"
out = here.parent / "cre8-landing" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html.replace(marker, "const IMG = " + json.dumps(imgs) + ";"), encoding="utf-8")
print(out, round(out.stat().st_size / 1024), "KB,", len(imgs), "images")
