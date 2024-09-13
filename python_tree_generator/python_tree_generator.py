"""This module provides Python Tree Generator main module."""

import pathlib
import sys
from collections import deque

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class DirectoryTree:
    def __init__(
        self, 
        root_dir: pathlib.Path,
        excluded_dirs: list[str],
        excluded_files: list[str], 
        dir_only: bool=False, 
        output_file=sys.stdout
    ):
        self._output_file = output_file
        self._excluded_dirs = excluded_dirs
        self._excluded_files = excluded_files
        self._generator = _TreeGenerator(root_dir, excluded_dirs, excluded_files, dir_only)

    def generate(self):
        tree = self._generator.build_tree()
        if self._output_file != sys.stdout:
            # Wrap the tree in a markdown code block
            tree.appendleft("```")
            tree.append("```")
            self._output_file = open(self._output_file, mode="w", encoding="UTF-8")
        with self._output_file as stream:
            for entry in tree:
                print(entry, file=stream)


class _TreeGenerator:
    def __init__(
        self,
        root_dir: pathlib.Path,
        excluded_dirs: list[str],
        excluded_files:list[str],
        dir_only: bool=False
    ):
        self._root_dir = pathlib.Path(root_dir)
        self._dir_only = dir_only
        self._excluded_dirs = excluded_dirs
        self._excluded_files = excluded_files
        self._tree = deque()

    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _tree_head(self):
        self._tree.append(f"📂 {self._root_dir}")

    def _tree_body(self, directory: pathlib.Path, prefix: str=""):
        entries = self._prepare_entries(directory)
        last_index = len(entries) - 1
        for index, entry in enumerate(entries):
            connector = ELBOW if index == last_index else TEE
            if entry.is_dir():
                self._add_directory(entry, index, last_index, prefix, connector)
            else:
                self._add_file(entry, prefix, connector)

    def _prepare_entries(self, directory: pathlib.Path):
        entries = sorted(directory.iterdir(), key=lambda entry: str(entry))
        if self._dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
        else:
            entries = sorted(entries, key=lambda entry: entry.is_file())
        return self._remove_excluded(entries)

    def _remove_excluded(self, entries: list[pathlib.Path]):
        return [
            entry for entry in entries
            if (entry.is_dir() and entry.name not in self._excluded_dirs)
            or (entry.is_file() and entry.name not in self._excluded_files)
        ]

    def _add_directory(self, directory, index, last_index, prefix, connector):
        if directory.name in self._excluded_dirs:
            return

        self._tree.append(f"{prefix}{connector} 📂 {directory.name}")
        if index != last_index:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._tree_body(directory=directory, prefix=prefix)

    def _add_file(self, file, prefix, connector):
        if file.name in self._excluded_files:
            return
        self._tree.append(f"{prefix}{connector} 📄 {file.name}")
