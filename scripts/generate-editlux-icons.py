#!/usr/bin/env python3
"""Generate Editlux PNG application icons from simple vector-like primitives."""

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]


def interpolate(start: tuple[int, int, int], end: tuple[int, int, int], value: float):
    return tuple(round(a + (b - a) * value) for a, b in zip(start, end))


def make_icon(size: int) -> Image.Image:
    scale = size / 320
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    def box(values):
        return tuple(round(value * scale) for value in values)

    draw.rounded_rectangle(box((12, 12, 308, 308)), radius=round(68 * scale), fill="#15171c")
    draw.rounded_rectangle(
        box((31, 31, 289, 289)),
        radius=round(52 * scale),
        outline="#2b3038",
        width=max(1, round(6 * scale)),
    )

    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.polygon(
        [
            box((82, 77)),
            box((238, 77)),
            box((238, 118)),
            box((130, 118)),
            box((130, 143)),
            box((224, 143)),
            box((224, 180)),
            box((130, 180)),
            box((130, 207)),
            box((238, 207)),
            box((238, 248)),
            box((82, 248)),
        ],
        fill=255,
    )
    gradient = Image.new("RGBA", (size, size))
    gradient_pixels = gradient.load()
    for y in range(size):
        for x in range(size):
            ratio = (x + y) / max(1, 2 * size - 2)
            gradient_pixels[x, y] = (*interpolate((0, 224, 192), (0, 166, 255), ratio), 255)
    image.alpha_composite(Image.composite(gradient, Image.new("RGBA", image.size), mask))

    draw = ImageDraw.Draw(image)
    draw.polygon([box((177, 132)), box((235, 161)), box((177, 190))], fill="#f7fbff")
    return image


def main() -> None:
    outputs = {
        320: ROOT / "icons/editlux-logo-320x320.png",
        64: ROOT / "icons/editlux-logo-64.png",
        128: ROOT / "packaging/linux/icons/128x128/io.github.editlux.Editlux.png",
    }
    outputs[64].parent.mkdir(parents=True, exist_ok=True)
    outputs[128].parent.mkdir(parents=True, exist_ok=True)
    for size, path in outputs.items():
        make_icon(size).save(path, optimize=True)
    make_icon(64).save(
        ROOT / "packaging/linux/icons/64x64/io.github.editlux.Editlux.png", optimize=True
    )


if __name__ == "__main__":
    main()
