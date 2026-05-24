import os
import re

from setuptools import setup


with open(os.path.abspath("./README.md"), "r", encoding="utf-8") as file:
    readme = file.read()

with open(os.path.abspath("./server/__init__.py"), "r", encoding="utf-8") as file:
    init_py = file.read()

version = re.search(r'__version__\s*=\s*[\'"]([^\'"]+)[\'"]', init_py).group(1)
author = re.search(r'__author__\s*=\s*[\'"]([^\'"]+)[\'"]', init_py).group(1)
license_ = re.search(r'__license__\s*=\s*[\'"]([^\'"]+)[\'"]', init_py).group(1)

setup(
    name="dpy-http-server",
    version=version,
    description="Efficiently and intuitively create and manage an HTTP web server running in tandem with a discord.py library bot",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/marwynnsomridhivej/dpy-http-server",
    author=author,
    license=license_,
    packages=["server"],
    include_package_data=True,
    install_requires=[
        "aiohttp",
    ],
)
