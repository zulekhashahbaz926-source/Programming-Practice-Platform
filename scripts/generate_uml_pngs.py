from PIL import Image, ImageDraw, ImageFont

FONT = ImageFont.load_default()

WIDTH = 1600
HEIGHT = 900

OUTPUT = {
    "use_case": "docs/uml_use_case.png",
    "class_diagram": "docs/uml_class_diagram.png",
    "activity": "docs/uml_activity_diagram.png",
    "sequence": "docs/uml_sequence_diagram.png",
}


def draw_arrow(draw, start, end, width=4, color="black"):
    draw.line([start, end], fill=color, width=width)
    # Draw arrowhead
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = (dx * dx + dy * dy) ** 0.5
    if length == 0:
        return
    ux = dx / length
    uy = dy / length
    size = 16
    perp = (-uy, ux)
    p1 = (end[0] - ux * size + perp[0] * size / 2, end[1] - uy * size + perp[1] * size / 2)
    p2 = (end[0] - ux * size - perp[0] * size / 2, end[1] - uy * size - perp[1] * size / 2)
    draw.polygon([end, p1, p2], fill=color)


def centered_text(draw, text, box, font=FONT, fill="black"):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = box[0] + (box[2] - box[0] - w) / 2
    y = box[1] + (box[3] - box[1] - h) / 2
    draw.text((x, y), text, font=font, fill=fill)


def draw_oval(draw, box, outline="black", width=4):
    draw.ellipse(box, outline=outline, width=width)


def draw_rectangle(draw, box, outline="black", width=4):
    draw.rectangle(box, outline=outline, width=width)


def ensure_docs_dir():
    import os

    os.makedirs("docs", exist_ok=True)


def create_use_case():
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    # Actor icons
    actor_left = (120, 220)
    draw.ellipse((actor_left[0] - 30, actor_left[1] - 30, actor_left[0] + 30, actor_left[1] + 30), outline="black", width=4)
    draw.line((actor_left[0], actor_left[1] + 30, actor_left[0], actor_left[1] + 120), fill="black", width=4)
    draw.line((actor_left[0], actor_left[1] + 50, actor_left[0] - 40, actor_left[1] + 100), fill="black", width=4)
    draw.line((actor_left[0], actor_left[1] + 50, actor_left[0] + 40, actor_left[1] + 100), fill="black", width=4)
    draw.line((actor_left[0], actor_left[1] + 70, actor_left[0] - 40, actor_left[1] + 70), fill="black", width=4)
    draw.text((actor_left[0] - 30, actor_left[1] + 130), "User", font=FONT, fill="black")

    actor_right = (1450, 220)
    draw.ellipse((actor_right[0] - 30, actor_right[1] - 30, actor_right[0] + 30, actor_right[1] + 30), outline="black", width=4)
    draw.line((actor_right[0], actor_right[1] + 30, actor_right[0], actor_right[1] + 120), fill="black", width=4)
    draw.line((actor_right[0], actor_right[1] + 50, actor_right[0] - 40, actor_right[1] + 100), fill="black", width=4)
    draw.line((actor_right[0], actor_right[1] + 50, actor_right[0] + 40, actor_right[1] + 100), fill="black", width=4)
    draw.line((actor_right[0], actor_right[1] + 70, actor_right[0] - 40, actor_right[1] + 70), fill="black", width=4)
    draw.text((actor_right[0] - 25, actor_right[1] + 130), "Admin", font=FONT, fill="black")

    # Ovals
    use_cases = [
        (540, 180, 960, 280, "Login / Register"),
        (540, 340, 960, 440, "View Dashboard"),
        (540, 500, 960, 600, "Run Tests"),
        (540, 660, 960, 760, "Peer Review"),
    ]
    for x1, y1, x2, y2, text in use_cases:
        draw_oval(draw, (x1, y1, x2, y2), outline="black", width=4)
        centered_text(draw, text, (x1, y1, x2, y2), font=FONT)

    # Arrows
    arrow_positions = [200, 360, 520, 680]
    for y, case in zip(arrow_positions, use_cases):
        x_start, y_start = actor_left[0] + 30, actor_left[1] + 30 + (y - 200)
        x_end, y_end = case[0], (case[1] + case[3]) / 2
        draw_arrow(draw, (x_start, y_start), (x_end, y_end))

    draw_arrow(draw, (actor_right[0] - 30, actor_right[1] + 60), (use_cases[1][2], (use_cases[1][1] + use_cases[1][3]) / 2))

    centered_text(draw, "Zyntriva Use Case Diagram", (0, 20, WIDTH, 80), font=FONT, fill="black")
    img.save(OUTPUT["use_case"])


def create_class_diagram():
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    classes = {
        "ZyntrivaApp": (100, 120, 420, 260, ["main()", "show_frame(name)", "-current_user", "-db"]),
        "AuthView": (100, 360, 420, 520, ["build_interface()", "login_user()", "register_user()"]),
        "AuthController": (520, 120, 940, 260, ["register_user(...)", "authenticate_user(...)"]),
        "DatabaseManager": (520, 360, 940, 520, ["initialize_schema()", "create_user(...)", "get_commits()"]),
        "DashboardView": (1040, 120, 1460, 260, ["build_layout()", "render_module(name)", "update_stats()"]),
        "DashboardController": (1040, 360, 1460, 520, ["load_module_data(name)", "get_dashboard_stats()"]),
    }

    for name, entry in classes.items():
        x1, y1, x2, y2, attrs = entry
        draw_rectangle(draw, (x1, y1, x2, y2), outline="black", width=4)
        draw.rectangle((x1, y1, x2, y1 + 40), outline="black", width=4)
        centered_text(draw, name, (x1, y1, x2, y1 + 40), font=FONT)
        content_top = y1 + 50
        for i, attr in enumerate(attrs):
            draw.text((x1 + 12, content_top + i * 24), attr, font=FONT, fill="black")

    draw_arrow(draw, (420, 190), (520, 190))
    draw_arrow(draw, (420, 430), (520, 430))
    draw_arrow(draw, (940, 190), (1040, 190))
    draw_arrow(draw, (940, 430), (1040, 430))
    draw_arrow(draw, (250, 260), (250, 360))

    centered_text(draw, "Zyntriva Class Diagram", (0, 20, WIDTH, 80), font=FONT, fill="black")
    img.save(OUTPUT["class_diagram"])


def create_activity_diagram():
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    # Start node
    draw.ellipse((260, 180, 340, 260), outline="black", width=4)
    centered_text(draw, "Start", (260, 180, 340, 260), font=FONT)

    # Activities
    activities = [
        (560, 170, 1040, 250, "Enter Credentials"),
        (560, 290, 1040, 370, "Validate Input"),
        (560, 410, 1040, 490, "Authenticate User"),
        (560, 530, 1040, 610, "Load Dashboard"),
    ]
    for x1, y1, x2, y2, text in activities:
        draw_rectangle(draw, (x1, y1, x2, y2), outline="black", width=4)
        centered_text(draw, text, (x1, y1, x2, y2), font=FONT)

    # Decision diamond
    diamond = [(800, 380), (880, 450), (800, 520), (720, 450)]
    draw.polygon(diamond, outline="black", fill="white")
    centered_text(draw, "Valid?", (720, 380, 880, 520), font=FONT)

    draw_arrow(draw, (300, 220), (560, 220))
    draw_arrow(draw, (800, 250), (800, 380))
    draw_arrow(draw, (800, 450), (800, 530))
    draw_arrow(draw, (800, 530), (800, 610))
    draw_arrow(draw, (1040, 510), (1240, 510))
    draw.text((1060, 470), "No", font=FONT, fill="black")
    draw_arrow(draw, (1040, 450), (1240, 450))
    draw_arrow(draw, (1240, 450), (1240, 220))
    draw.text((1260, 410), "No", font=FONT, fill="black")

    centered_text(draw, "Zyntriva Activity Diagram", (0, 20, WIDTH, 80), font=FONT, fill="black")
    img.save(OUTPUT["activity"])


def create_sequence_diagram():
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    lifelines = {
        "User": 220,
        "AuthView": 520,
        "AuthController": 820,
        "DatabaseManager": 1120,
    }
    for name, x in lifelines.items():
        draw.text((x - 40, 80), name, font=FONT, fill="black")
        draw.line((x, 140, x, 760), fill="black", width=4)
        draw.line((x - 40, 100, x + 40, 100), fill="black", width=4)

    draw_arrow(draw, (240, 180), (520, 180))
    draw.text((360, 160), "submit credentials", font=FONT, fill="black")
    draw_arrow(draw, (520, 240), (820, 240))
    draw.text((620, 220), "authenticate()", font=FONT, fill="black")
    draw_arrow(draw, (820, 300), (1120, 300))
    draw.text((920, 280), "find_user()", font=FONT, fill="black")
    draw_arrow(draw, (1120, 360), (820, 360))
    draw.text((920, 340), "user_row", font=FONT, fill="black")
    draw_arrow(draw, (820, 420), (520, 420))
    draw.text((720, 400), "success", font=FONT, fill="black")
    draw_arrow(draw, (520, 480), (240, 480))
    draw.text((360, 460), "display dashboard", font=FONT, fill="black")

    centered_text(draw, "Zyntriva Sequence Diagram", (0, 20, WIDTH, 80), font=FONT, fill="black")
    img.save(OUTPUT["sequence"])


if __name__ == "__main__":
    ensure_docs_dir()
    create_use_case()
    create_class_diagram()
    create_activity_diagram()
    create_sequence_diagram()
    print("Saved UML PNGs to docs/")
