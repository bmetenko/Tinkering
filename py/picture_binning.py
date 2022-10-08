from PIL import Image
import argparse
import numpy as np
import matplotlib.pyplot as plt
import colorthief

parser = argparse.ArgumentParser(description="Image histogram creator.")

parser.add_argument("-i", "--image_path", dest="image_path", help="Image path", required=True)

def main():
    args = parser.parse_args()
    print(args)

    img = colorthief.ColorThief('%s'%(args.image_path))

    plt.imshow(([[img.get_color(quality=1)]]))
    

if __name__ == "__main__":
    main()