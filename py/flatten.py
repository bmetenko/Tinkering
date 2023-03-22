import argparse
import os
import shutil


def flatten_dir(input_dir, output_dir):
    all_combinations = {}
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Walk through the input directory and flatten it
    for root, _, files in os.walk(input_dir):
        for file in files:
            old_path = os.path.join(root, file)
            new_path = os.path.join(output_dir, file)
            all_combinations[old_path] = new_path
            shutil.copy2(old_path, new_path)

    return all_combinations


    print("Directory flattened successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flatten a directory")
    parser.add_argument("input_dir", type=str, help="The input directory to flatten")
    parser.add_argument("output_dir", type=str, help="The output directory to store flattened files")
    args = parser.parse_args()

    changes = flatten_dir(args.input_dir, args.output_dir)

    print(changes)

    # Missing some data, maybe due to copies?
    # Check.