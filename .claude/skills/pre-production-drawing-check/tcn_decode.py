#!/usr/bin/env python3
"""Decode a SmartCabinet -> TpaCAD job folder for the pre-production drawing check.

Usage:
  tcn_decode.py <folder>                 summary of every part (sizes, bores, profiles, macros)
  tcn_decode.py <folder> --diff <older>  same, but only parts whose bytes changed vs an older copy
  tcn_decode.py <file.TCN> [...]         decode single programs

Reads (all UTF-16 except the PDF):
  worklist.xmlst  -> LENGTH x HEIGHT x THICKNESS per program
  *.fnm           -> the part list SmartCabinet exported (plain text, not UTF-16)
  *.TCN           -> W#81 bores, W#89 profile starts, W#1001 'foro mul' rows (shelf-pin / Cabineo rows)
  *.pdf           -> cutting list via pdftotext (if installed)

Codes (as learned 2026-10-03, see Wiki/Processes/pre-production-drawing-check.md):
  W#81  bore:    #1 X, #2 Y, #3 depth (negative), #1002 diameter, WO=1 mirrored
  W#89  profile: #1 X, #2 Y, #3 depth, #205 tool, #40 type (1 = pocket, 2 = slot);
                 a Cabineo pocket starts 7.5 mm (one Ø15 radius) from its circle centre
  W#1001 row:    8510 start, 8511 end, 8512 pitch, 8513 depth, 8518 Y, 8522 diameter
  SIDE#1 = face A (top), SIDE#3 etc. = edges / other faces; files ending 'B' are the B face
"""
import glob, hashlib, os, re, subprocess, sys

def u16(path):
    b = open(path, 'rb').read()
    if b[:2] in (b'\xff\xfe', b'\xfe\xff'):           # UTF-16 with BOM (.TCN, worklist)
        return b.decode('utf-16', errors='replace')
    return b.decode('utf-8', errors='replace')         # the .fnm is plain text

def decode_tcn(path):
    t = u16(path)
    m = re.search(r'DL=([\d.]+) DH=([\d.]+) DS=([\d.]+)', t)
    dims = m.groups() if m else ('?', '?', '?')
    ops = []
    for side in re.split(r'SIDE#', t)[1:]:
        sn = side.split('{', 1)[0]
        for w in re.finditer(r'W#(\d+)\{ ::(\S+)([^}]*)\}W', side):
            code, _, body = w.groups()
            if code in ('2201', '2111'):          # line / arc segments of a profile
                continue
            kv = dict(re.findall(r'#(\d+)=(\S+)', body))
            if code == '81':
                ops.append(f"S{sn} BORE x{kv.get('1')} y{kv.get('2')} d{kv.get('3')} Ø{kv.get('1002')}"
                           + (' WO' if re.search(r'WO=1', body) else ''))
            elif code == '89':
                ops.append(f"S{sn} PROF x{kv.get('1')} y{kv.get('2')} d{kv.get('3')} T{kv.get('205')} type{kv.get('40')}")
            else:
                keep = ('8510', '8511', '8512', '8513', '8518', '8522', '1', '2', '3')
                ops.append(f"S{sn} W{code} " + ' '.join(f'{k}={v}' for k, v in kv.items() if k in keep))
    return dims, ops

def worklist(folder):
    p = os.path.join(folder, 'worklist.xmlst')
    if not os.path.exists(p):
        return []
    t = u16(p)
    rows = []
    for r in re.findall(r'<Row Index.*?</Row>', t, re.S):
        g = lambda n: (re.search(r'Name="' + n + r'"[^>]*>([^<]*)<', r) or [None, '?'])[1]
        rows.append((g('NAME'), g('LENGTH'), g('HEIGHT'), g('THICKNESS')))
    return rows

def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()

def main(argv):
    if not argv:
        print(__doc__); return
    if all(a.upper().endswith('.TCN') for a in argv):
        for p in argv:
            d, o = decode_tcn(p); print('=====', p, d); print('\n'.join(o))
        return
    folder = argv[0]
    older = argv[argv.index('--diff') + 1] if '--diff' in argv else None
    print('## worklist (L x H x T)')
    for r in worklist(folder):
        print('  ', *r)
    for f in glob.glob(os.path.join(folder, '*.fnm')):
        print('## .fnm parts:', ' '.join(u16(f).split()))
    for p in sorted(glob.glob(os.path.join(folder, '*.TCN'))):
        name = os.path.basename(p)
        if older:
            q = os.path.join(older, name)
            if os.path.exists(q) and md5(p) == md5(q):
                print('=====', name, 'SAME as older copy'); continue
            if not os.path.exists(q):
                print('=====', name, 'NEW')
        d, o = decode_tcn(p)
        print('=====', name, d); print('\n'.join(o))
    if older:
        for q in sorted(glob.glob(os.path.join(older, '*.TCN'))):
            if not os.path.exists(os.path.join(folder, os.path.basename(q))):
                print('=====', os.path.basename(q), 'REMOVED (was in older copy)')
    for pdf in glob.glob(os.path.join(folder, '*.pdf')):
        try:
            txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
            print('## cutting list:', os.path.basename(pdf))
            for line in txt.splitlines():
                if re.search(r'^\s*\d+ - |material|MATERIAL', line):
                    print('  ', re.sub(r'\s{2,}', '  ', line.strip()))
        except FileNotFoundError:
            print('## pdftotext not installed; read', pdf, 'by eye')

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except BrokenPipeError:
        pass
