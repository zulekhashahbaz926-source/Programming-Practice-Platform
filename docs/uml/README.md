This folder contains generated UML diagrams for the Weather Dashboard application.

Files:
- `component_diagram.png` — Component-level overview (UI, backend, services, DB)
- `sequence_fetch_weather.png` — Sequence diagram for fetching weather
- `activity_refresh.png` — Activity diagram for refresh flow

How to regenerate diagrams:

1. Install requirements (Pillow):

```powershell
pip install Pillow
```

2. Run the generator:

```powershell
python ..\..\scripts\generate_weather_uml.py
```

To export PNGs to PDFs, run the `scripts/export_uml_pdfs.py` script.
