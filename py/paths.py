from ast import main
from pathlib import Path
import os

def main():
    cwd0 = Path.cwd()
    cwd1 = os.getcwd()

    print(f"{cwd0=}, {cwd1=}: exact: {cwd0 == cwd1}")
    print(f"{cwd0.as_posix()=}, {cwd1=}: exact: {cwd0.as_posix() == cwd1}")

    

if __name__ == "__main__":
    main()