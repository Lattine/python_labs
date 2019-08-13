# -*- coding: utf-8 -*-

# @Time    : 2019/8/13
# @Author  : Lattine

# ======================

import os
import argparse
from pdf2image import convert_from_path


def check_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def main_process(args):
    pdf = args.pdf
    output_dir = args.output
    image = args.image
    fmt = args.fmt

    check_dir(output_dir)
    convert_from_path(pdf, 300, output_folder=output_dir, fmt=fmt, output_file=image, thread_count=1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=str, default="data/1.pdf", help="PDF path.")
    parser.add_argument("--output", type=str, default="output", help="OUTPUT path.")
    parser.add_argument("--image", type=str, default="demo", help="image file name")
    parser.add_argument("--fmt", type=str, default="png", help="image type.")

    args = parser.parse_args()
    main_process(args)
