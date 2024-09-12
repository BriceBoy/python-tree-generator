import pathlib
from setuptools import setup

from python_tree_generator import __version__

HERE = pathlib.Path().cwd()
DESCRIPTION = HERE.joinpath("README.md").read_text()
VERSION = __version__


setup(
    name="python-tree-generator",
    version=VERSION,
    description="Generate markdown directory tree",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/BriceBoy/python-tree-generator",
    author="BriceBoy",
    author_email="piqueux.brice@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=["python_tree_generator"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "tree-gen=python_tree_generator.__main__:main",
        ]
    },
)
