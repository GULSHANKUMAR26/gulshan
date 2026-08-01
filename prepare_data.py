import argparse
from pathlib import Path

import numpy as np
from PIL import Image


def find_images(root_dir, extensions=(".png", ".jpg", ".jpeg", ".bmp", ".gif")):
    root = Path(root_dir)
    for path in root.rglob("*"):
        if path.suffix.lower() in extensions and path.is_file():
            yield path


def load_dataset(data_dir, image_size=(224, 224), grayscale=False):
    data_dir = Path(data_dir)
    if not data_dir.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    X = []
    y = []
    classes = []

    class_dirs = [p for p in sorted(data_dir.iterdir()) if p.is_dir()]
    if not class_dirs:
        raise ValueError(f"No class subdirectories found in {data_dir}")

    for class_dir in class_dirs:
        classes.append(class_dir.name)
        for image_path in find_images(class_dir):
            try:
                image = Image.open(image_path)
                if grayscale:
                    image = image.convert("L")
                else:
                    image = image.convert("RGB")
                image = image.resize(image_size, Image.BILINEAR)
                array = np.asarray(image, dtype=np.uint8)
                X.append(array)
                y.append(class_dir.name)
            except Exception as exc:
                print(f"Skipping file {image_path}: {exc}")

    if not X:
        raise ValueError(f"No images loaded from {data_dir}")

    X = np.stack(X)
    y = np.array(y, dtype=object)
    classes = np.array(classes, dtype=object)
    return X, y, classes


def save_dataset(output_path, X, y, classes):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(output_path, X=X, y=y, classes=classes)
    print(f"Saved dataset to {output_path}.npz")


def parse_args():
    parser = argparse.ArgumentParser(description="Prepare image dataset for training.")
    parser.add_argument("data_dir", help="Root directory containing class subfolders")
    parser.add_argument("--output", default="prepared_data", help="Output file prefix for the .npz file")
    parser.add_argument("--width", type=int, default=224, help="Output image width")
    parser.add_argument("--height", type=int, default=224, help="Output image height")
    parser.add_argument("--grayscale", action="store_true", help="Convert images to grayscale")
    return parser.parse_args()


def main():
    args = parse_args()
    X, y, classes = load_dataset(args.data_dir, image_size=(args.width, args.height), grayscale=args.grayscale)
    save_dataset(args.output, X, y, classes)


if __name__ == "__main__":
    main()
