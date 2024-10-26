import svgwrite
import sys


def generate_progress_bar(filename, progress):
    # Validate progress value
    if not (0 <= progress <= 1):
        raise ValueError("Progress value must be between 0 and 1.")

    # SVG dimensions
    width = 300
    height = 40

    # Create SVG Drawing
    dwg = svgwrite.Drawing(filename, size=(width, height))

    # Background rectangle
    background = dwg.rect(insert=(0, 0), size=(width, height), rx=5, ry=5, fill='#E74C3C')
    dwg.add(background)

    # Progress bar rectangle
    progress_width = int(width * progress)
    # print(f"{progress_width=}")
    progress_bar = dwg.rect(insert=(0, 0), size=(progress_width, height), rx=5, ry=5, fill='#2ECC71')
    dwg.add(progress_bar)

    # Text label
    label = dwg.text(f'{progress * 100:.1f}%', insert=(10, height/2), fill='black', font_size=16)
    dwg.add(label)

    # Save SVG file
    dwg.save()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python generate_progress_bar.py <parameter>")
        sys.exit(1)

    generate_progress_bar('./.python/progress_bar.svg', float(sys.argv[1]))
