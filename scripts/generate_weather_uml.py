from PIL import Image, ImageDraw, ImageFont
import os

FONT = ImageFont.load_default()
WIDTH = 2400
HEIGHT = 1600
OUT_DIR = "docs/uml"
os.makedirs(OUT_DIR, exist_ok=True)


def draw_arrow(draw, start, end, width=6, color="black"):
    draw.line([start, end], fill=color, width=width)
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = (dx*dx+dy*dy)**0.5
    if length == 0:
        return
    ux = dx/length
    uy = dy/length
    size = 28
    perp = (-uy, ux)
    p1 = (end[0]-ux*size+perp[0]*size/2, end[1]-uy*size+perp[1]*size/2)
    p2 = (end[0]-ux*size-perp[0]*size/2, end[1]-uy*size-perp[1]*size/2)
    draw.polygon([end,p1,p2], fill=color)


def rect_mid(box):
    x1,y1,x2,y2 = box
    return ((x1+x2)/2, (y1+y2)/2)

def rect_side(box, side):
    x1,y1,x2,y2 = box
    if side=="left":
        return (x1, (y1+y2)/2)
    if side=="right":
        return (x2, (y1+y2)/2)
    if side=="top":
        return ((x1+x2)/2, y1)
    return ((x1+x2)/2, y2)


def centered_text(draw, text, box, font=FONT, fill="black"):
    bbox = draw.textbbox((0,0), text, font=font)
    w = bbox[2]-bbox[0]
    h = bbox[3]-bbox[1]
    x = box[0]+(box[2]-box[0]-w)/2
    y = box[1]+(box[3]-box[1]-h)/2
    draw.text((x,y), text, font=font, fill=fill)


def create_component():
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    # UI box
    ui = (180, 200, 700, 420)
    draw.rectangle(ui, outline="black", width=6)
    centered_text(draw, "Tkinter UI\nWeatherDashboardApp\nViews", ui)

    # Backend
    backend = (900, 160, 1500, 520)
    draw.rectangle(backend, outline="black", width=6)
    centered_text(draw, "Backend\nController, Cache, DB", backend)

    # Services
    wsvc = (1700, 140, 2300, 320)
    draw.rectangle(wsvc, outline="black", width=6)
    centered_text(draw, "Weather API\nService", wsvc)

    notif = (1700, 380, 2300, 560)
    draw.rectangle(notif, outline="black", width=6)
    centered_text(draw, "Notification\nService", notif)

    analytics = (1700, 620, 2300, 800)
    draw.rectangle(analytics, outline="black", width=6)
    centered_text(draw, "Analytics\nService", analytics)

    prefs = (1700, 860, 2300, 1040)
    draw.rectangle(prefs, outline="black", width=6)
    centered_text(draw, "User Preferences\nService", prefs)

    # DB
    db = (900, 600, 1200, 820)
    draw.rectangle(db, outline="black", width=6)
    centered_text(draw, "SQLite DB", db)

    # arrows
    draw_arrow(draw, rect_side(ui, "right"), rect_side(backend, "left"))
    draw_arrow(draw, rect_side(backend, "right"), rect_side(wsvc, "left"))
    draw_arrow(draw, rect_side(backend, "right"), rect_side(notif, "left"))
    draw_arrow(draw, rect_side(backend, "right"), rect_side(analytics, "left"))
    draw_arrow(draw, rect_side(backend, "right"), rect_side(prefs, "left"))
    draw_arrow(draw, rect_side(backend, "bottom"), rect_side(db, "top"))

    centered_text(draw, "Component Diagram - Weather Dashboard", (0,30,WIDTH,110))
    img.save(os.path.join(OUT_DIR, "component_diagram.png"), dpi=(300,300))


def create_sequence():
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    # lifelines positions
    xs = [300, 900, 1500, 2100]
    names = ["User","UI","Backend","WeatherAPI"]
    for x,name in zip(xs,names):
        draw.text((x-80,140), name, fill="black")
        draw.line((x,200,x,1400), fill="black", width=4)

    # arrows
    draw_arrow(draw, (xs[0],260),(xs[1],260))
    draw.text(((xs[0]+xs[1])/2-60,240), "click Refresh", fill="black")
    draw_arrow(draw, (xs[1],340),(xs[2],340))
    draw.text(((xs[1]+xs[2])/2-60,320), "fetch_weather(location)", fill="black")
    draw_arrow(draw, (xs[2],420),(xs[3],420))
    draw.text(((xs[2]+xs[3])/2-80,400), "GET /weather?loc=", fill="black")
    draw_arrow(draw, (xs[3],500),(xs[2],500))
    draw.text(((xs[2]+xs[3])/2-40,480), "200 {data}", fill="black")
    draw_arrow(draw, (xs[2],580),(xs[1],580))
    draw.text(((xs[1]+xs[2])/2-40,560), "render(data)", fill="black")
    draw_arrow(draw, (xs[1],660),(xs[0],660))
    draw.text(((xs[0]+xs[1])/2-40,640), "display\nforecast", fill="black")

    centered_text(draw, "Sequence Diagram - Fetch Weather", (0,30,WIDTH,110))
    img.save(os.path.join(OUT_DIR, "sequence_fetch_weather.png"), dpi=(300,300))


def create_activity():
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    boxes = [ (120,220,600,320,'Start'), (120,360,600,460,'Enter Location'), (120,500,600,600,'Check Cache'), (800,500,1280,600,'Call API'), (120,660,600,760,'Render') ]
    for b in boxes:
        draw.rectangle(b[:4], outline='black', width=6)
        centered_text(draw, b[4], b[:4])

    # arrows midpoints
    draw_arrow(draw, rect_side(boxes[0][:4],'bottom'), rect_side(boxes[1][:4],'top'))
    draw_arrow(draw, rect_side(boxes[1][:4],'bottom'), rect_side(boxes[2][:4],'top'))
    draw_arrow(draw, rect_side(boxes[2][:4],'right'), rect_side(boxes[3][:4],'left'))
    draw_arrow(draw, rect_side(boxes[3][:4],'left'), rect_side(boxes[4][:4],'top'))

    centered_text(draw, "Activity - Refresh Flow", (0,30,WIDTH,110))
    img.save(os.path.join(OUT_DIR, "activity_refresh.png"), dpi=(300,300))


if __name__ == '__main__':
    create_component()
    create_sequence()
    create_activity()
    print('Saved diagrams to', OUT_DIR)
