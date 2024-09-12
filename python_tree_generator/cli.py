"""This module provides the Python Tree Generator CLI."""

import argparse
import sys

from . import __version__


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
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
    )
    return parser.parse_args()
