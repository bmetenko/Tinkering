import re
from enum import Enum, auto
from typing import Union, Iterable
import itertools

import argparse
import numpy as np
import matplotlib.pyplot as plt
import colorthief
import pandas as pd


class PalCalc(Enum):
    Sum = auto()
    Mean = auto()
    Multiply = auto()
    Matrix = auto()
    

def rgb_distance(x: tuple[int, int, int], y: tuple[int, int, int]) -> float:
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

def heatmap(array: np.ndarray, cmap='viridis'):
    fig, ax = plt.subplots()
    im = ax.imshow(array, cmap=cmap)
    ax.figure.colorbar(im)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            text = ax.text(j, i, np.round(array[i, j]),
            ha="center", va="center", color="w")
    plt.show()


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

    palette_data = {}
    for img_path in images_to_check:
        img = colorthief.ColorThief('%s' % img_path)

        img_short = re.split("/", img_path)[-1]
        # input("Press [enter] to continue.")

        palette_data[img_short] = img.get_palette(5)

    print(palette_data)

    palette_frame = pd.DataFrame(palette_data)
    stacked_palettes = [
        palette_frame.iloc[:, i].to_list()
        for i in range(len(palette_frame.columns))
    ]

    plt.imshow(stacked_palettes)
    
    plt.pause(0.01)

    ## Simple two palette heatmap, how to handle odd ones?
    ## How to make this useful.
    if len(stacked_palettes) >= 2:
        heatmap(
            palette_distance(
                stacked_palettes[0], stacked_palettes[1], 5, PalCalc.Matrix
                )
            )

        file_grid = np.stack(
            list(itertools.combinations(images_to_check, r=2))
            ).tolist()

        print(file_grid)


if __name__ == "__main__":
    main()
