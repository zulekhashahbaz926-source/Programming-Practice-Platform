import os
from cairosvg import svg2png

IN_DIR = 'docs/uml'
OUT_DIR = IN_DIR
os.makedirs(OUT_DIR, exist_ok=True)

for fname in os.listdir(IN_DIR):
    if fname.lower().endswith('.svg'):
        in_path = os.path.join(IN_DIR, fname)
        out_name = os.path.splitext(fname)[0] + '.png'
        out_path = os.path.join(OUT_DIR, out_name)
        try:
            svg2png(url=in_path, write_to=out_path, output_width=2400, output_height=None)
            print('Converted', in_path, '->', out_path)
        except Exception as e:
            print('Failed to convert', in_path, e)
