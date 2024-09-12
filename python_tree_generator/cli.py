"""This module provides the Python Tree Generator CLI."""

import argparse
import sys

from . import __version__


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree-gen",
        description="Python Tree Generator, a directory tree generator",
        epilog="Thanks for using Python Tree Generator!",
    )
    parser.version = f"Python Tree Generator v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="generate a full directory tree starting at ROOT_DIR",
    )
    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="generate a directory-only tree",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        metavar="OUTPUT_FILE",
        nargs="?",
        default=sys.stdout,
        help="generate a full directory tree and save it to a file",
    ),
    parser.add_argument(
        "-ed",
        "--exclude-dir",
        metavar="EXCLUDED_DIR",
        action="append",
        default=[],
        help="exclude directories from the tree generation (can be used multiple times)"
    ),
    parser.add_argument(
        "-ef",
        "--exclude-file",
        metavar="EXCLUDED_FILE",
        action="append",
        default=[],
        help="exclude files from the tree generation (can be used multiple times)"
    ),
    return parser.parse_args()
