from PIL import Image
import argparse
import numpy as np
import matplotlib.pyplot as plt
import colorthief

def rgb_distance(x: tuple[int], y: tuple[int]):
    r1, g1, b1 = x
    r2, g2, b2 = y
    
    d = np.sqrt((
        r2-r1)**2+(g2-g1)**2+(b2-b1)**2
    )

    return d

def palette_distance(pal1, pal2, check_iterations=1):

    max_iterations = min(len(pal1), len(pal2))

    if max_iterations == 0:
        raise IndexError("Can't compare with empty palettes.")

    if max_iterations < check_iterations:
        check_iterations = max_iterations

    out = 0

    for i in range(check_iterations):
        out += rgb_distance(pal1[i], pal2[1])

    return out

parser = argparse.ArgumentParser(description="Image histogram creator.")

parser.add_argument("-i", "--image_path", dest="image_path", help="Image path", required=True)

def main():
    args = parser.parse_args()
    print(args)

    img = colorthief.ColorThief('%s'%(args.image_path))

    plt.imshow(([[img.get_color(quality=1)]]))

    plt.imshow([[i for i in img.get_palette(5)]])



if __name__ == "__main__":
    main()