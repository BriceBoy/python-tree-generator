"""This module provides the Python Tree Generator CLI."""

import pathlib
import sys

from .cli import parse_cmd_line_arguments
from .python_tree_generator import DirectoryTree


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    tree = DirectoryTree(
        root_dir,
        dir_only=args.dir_only,
        output_file=args.output_file,
        excluded_dirs=args.exclude_dir,
        excluded_files=args.exclude_file
    )
    tree.generate()


if __name__ == "__main__":
    main()
