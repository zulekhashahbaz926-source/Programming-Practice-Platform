from PIL import Image
import os

IN_DIR = 'docs/uml'
OUT_DIR = IN_DIR
for fname in os.listdir(IN_DIR):
    if fname.lower().endswith('.png'):
        path = os.path.join(IN_DIR, fname)
        img = Image.open(path).convert('RGB')
        pdf_name = os.path.splitext(fname)[0] + '.pdf'
        out_path = os.path.join(OUT_DIR, pdf_name)
        try:
            img.save(out_path)
            print('Saved', out_path)
        except Exception as e:
            print('Skipping PDF for', fname, '— conversion failed:', e)
