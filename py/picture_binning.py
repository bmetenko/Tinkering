from ast import arg
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description="Image histogram creator.")

parser.add_argument("-i", "--image_path", dest="image_path", help="Image path", required=True)

def main():
    args = parser.parse_args()
    print(args)

    img = Image.open('%s'%(args.image_path))
    print(img)
    

if __name__ == "__main__":
    main()