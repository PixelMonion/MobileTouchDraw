from svgpathtools import svg2paths
import sys

def convert_svg_to_touch(svg_path, output_script, scale=1.0, offset_x=0, offset_y=0):
    paths, _ = svg2paths(svg_path)

    with open(output_script, "w") as f:
        for path in paths:
            points = []
            for seg in path:
                for t in [i / 100.0 for i in range(101)]:
                    point = seg.point(t)
                    x = int(point.real * scale + offset_x)
                    y = int(point.imag * scale + offset_y)
                    points.append((x, y))

            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i + 1]
                f.write(f"input swipe {x1} {y1} {x2} {y2} 10\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 svg_to_touch.py input.svg output.sh")
        sys.exit(1)

    convert_svg_to_touch(sys.argv[1], sys.argv[2])
