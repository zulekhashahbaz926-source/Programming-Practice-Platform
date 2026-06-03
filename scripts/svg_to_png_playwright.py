import asyncio
from playwright.async_api import async_playwright
from pathlib import Path

async def convert_svg_to_png():
    """Convert SVG files to PNG using Playwright browser screenshot."""
    
    svg_files = [
        'class_diagram.svg',
        'use_case_diagram.svg',
        'sequence_diagram.svg',
        'activity_diagram.svg',
    ]
    
    base_path = Path('docs/uml')
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        for svg_file in svg_files:
            svg_path = base_path / svg_file
            png_path = base_path / svg_file.replace('.svg', '.png')
            
            if svg_path.exists():
                try:
                    page = await browser.new_page(viewport={'width': 2400, 'height': 2000})
                    file_url = svg_path.resolve().as_uri()
                    await page.goto(file_url)
                    
                    # Get the actual content dimensions
                    dimensions = await page.evaluate("""
                        () => {
                            const svg = document.querySelector('svg');
                            if (svg) {
                                return {
                                    width: svg.viewBox.baseVal.width || svg.width.baseVal.value,
                                    height: svg.viewBox.baseVal.height || svg.height.baseVal.value
                                };
                            }
                            return {width: 2400, height: 2000};
                        }
                    """)
                    
                    # Set viewport to match SVG dimensions
                    await page.set_viewport_size(width=int(dimensions['width']), height=int(dimensions['height']))
                    await page.screenshot(path=str(png_path))
                    print(f'Created {png_path.name} ({dimensions["width"]}x{dimensions["height"]}px)')
                    await page.close()
                    
                except Exception as e:
                    print(f'Error converting {svg_file}: {e}')
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(convert_svg_to_png())
