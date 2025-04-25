# MobileTouchDraw

MobileTouchDraw converts SVG paths to touch input commands on rooted Android devices.

## Usage

1. Install Termux, Python, svgpathtools.
2. Put SVG files in samples/ and run:

```bash
python3 svg_to_touch.py samples/spiral.svg samples/draw_spiral.sh
su
sh samples/draw_spiral.sh
```

## Requirements

- Rooted Android
- Termux
- Python
- svgpathtools
