from enum import Enum, auto
from typing import Union, Iterable

from PIL import Image
import argparse
import numpy as np
import matplotlib.pyplot as plt
import colorthief

class PalCalc(Enum):
    Sum = auto()
    Mean = auto()
    Multiply = auto()
    Matrix = auto()
    

def rgb_distance(x: tuple[int], y: tuple[int]):
    r1, g1, b1 = x
    r2, g2, b2 = y

    d = np.sqrt(
        (r2-r1)**2 + (g2-g1)**2 + (b2-b1)**2
    )

    return d

def palette_distance(
    pal1, 
    pal2, 
    check_iterations: int = 1,
    calculation: PalCalc = PalCalc.Sum
    ) -> Union[float, np.array]:

    max_iterations = min(len(pal1), len(pal2))

    if max_iterations == 0:
        raise IndexError("Can't compare with empty palettes.")

    if max_iterations < check_iterations:
        check_iterations = max_iterations

    out = 0 if calculation == PalCalc.Sum else 1

    
    if calculation == PalCalc.Sum:
        for i in range(check_iterations):
            out += rgb_distance(pal1[i], pal2[i])
        
    if calculation == PalCalc.Multiply:
        for i in range(check_iterations):
            out *= rgb_distance(pal1[i], pal2[i]) 

    if calculation == PalCalc.Mean:
        out = np.mean(
            [
                rgb_distance(pal1[x], pal2[x]) 
                for x in range(max_iterations)
            ]
        )

    if calculation == PalCalc.Matrix:
        # expand.grid like to matrix
        out = np.array(
            [
                rgb_distance(pal1[x], pal2[y]) 
                for x in range(max_iterations)
                for y in range(max_iterations)
            ]
        ).reshape(
            max_iterations, max_iterations
        )

    return out

parser = argparse.ArgumentParser(description="Image histogram creator.")

parser.add_argument(
    "-i", 
    "--image_path", 
    dest="image_path", 
    help="Image path", 
    required=True,
    nargs='*'
    )

def main():
    args = parser.parse_args()
    print(args)

    images_to_check = args.image_path

    if not isinstance(images_to_check, Iterable):
        images_to_check = [images_to_check]

    for img_path in args.image_path:
        img = colorthief.ColorThief('%s' % img_path)

        plt.imshow(([[img.get_color(quality=1)]]))

        plt.imshow([[i for i in img.get_palette(5)]])
        plt.pause(0.001)
        input("Press [enter] to continue.")



if __name__ == "__main__":
    main()