"""List a CAD PDF's dimension lines (magenta strokes) with their length in PDF points.
Usage: pdftocairo -svg plan.pdf plan.svg ; python3 -I pdf_dims.py plan.svg
Divide each dimension's written value (mm) by its length (pt) to get mm per point — the drawing's true scale.
Also prints long black wall segments (> 60 pt) with end points, to set up a coordinate frame."""
import re, math, sys
s = open(sys.argv[1]).read()
dims, walls = [], []
for p in re.findall(r'<path ([^>]*)/>', s):
    st = re.search(r'stroke="([^"]+)"', p); d = re.search(r' d="([^"]+)"', p)
    tr = re.search(r'transform="matrix\(([^)]+)\)"', p)
    if not (st and d): continue
    pts = [(float(a), float(b)) for a, b in re.findall(r'[ML] ?(-?[\d.]+) (-?[\d.]+)', d.group(1))]
    if tr:
        a, b, c, dd, e, f = map(float, re.split(r'[ ,]+', tr.group(1).strip()))
        pts = [(a*x+c*y+e, b*x+dd*y+f) for x, y in pts]
    for i in range(len(pts)-1):
        (x1, y1), (x2, y2) = pts[i], pts[i+1]; L = math.hypot(x2-x1, y2-y1)
        row = (round(L, 2), round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1))
        if '100%, 0%, 100%' in st.group(1): dims.append(row)
        elif 'rgb(0%, 0%, 0%)' in st.group(1) and L > 60: walls.append(row)
print('dimension lines (pt, x1,y1,x2,y2):'); [print(r) for r in sorted(dims, reverse=True)[:15]]
print('long wall segments:'); [print(r) for r in sorted(walls, reverse=True)[:25]]
