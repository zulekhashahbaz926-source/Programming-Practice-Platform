import os
from pathlib import Path

# These SVG diagrams need to be converted to PNG
# Since cairosvg requires system Cairo library which isn't available,
# we'll document the process for users to convert manually using online tools
# or they can use:
# 1. ImageMagick: magick convert input.svg output.png
# 2. Inkscape: inkscape input.svg -o output.png
# 3. Online converters: https://cloudconvert.com/svg-to-png

svg_files = [
    'docs/uml/class_diagram.svg',
    'docs/uml/use_case_diagram.svg',
    'docs/uml/sequence_diagram.svg',
    'docs/uml/activity_diagram.svg',
]

print("SVG to PNG conversion guide:")
print("=" * 60)
for svg_file in svg_files:
    if Path(svg_file).exists():
        png_file = svg_file.replace('.svg', '.png')
        print(f"\n{Path(svg_file).name} -> {Path(png_file).name}")
        print(f"  Windows (ImageMagick): magick convert {svg_file} {png_file}")
        print(f"  Linux/Mac: convert {svg_file} {png_file}")
        print(f"  Or use Inkscape: inkscape {svg_file} -o {png_file}")
