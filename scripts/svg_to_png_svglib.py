from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from pathlib import Path
import os

IN_DIR = 'docs/uml'
svg_files = [
    'class_diagram.svg',
    'use_case_diagram.svg',
    'sequence_diagram.svg',
    'activity_diagram.svg',
]

os.makedirs(IN_DIR, exist_ok=True)

for svg_name in svg_files:
    svg_path = Path(IN_DIR) / svg_name
    png_name = svg_name.replace('.svg', '.png')
    png_path = Path(IN_DIR) / png_name
    
    if svg_path.exists():
        try:
            # Convert SVG to ReportLab drawing
            drawing = svg2rlg(str(svg_path))
            if drawing:
                # Save as PNG
                renderPM.drawToFile(drawing, str(png_path), fmt='PNG', dpi=300)
                print(f'Converted {svg_name} -> {png_name}')
            else:
                print(f'Failed to parse {svg_name}')
        except Exception as e:
            print(f'Error converting {svg_name}: {e}')
    else:
        print(f'File not found: {svg_path}')
