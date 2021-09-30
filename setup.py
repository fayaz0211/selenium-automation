import sys

from setuptools import setup

assert sys.version_info >= (3, 6, 0), "selenium_utils requires Python 3.6+"
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta

setup(
    name="selenium_utils",
    description="A python library to add selenium utils to apps",
    url="https://github.com/fayaz0211/selenium-utils",
    license="MIT",
    packages=["selenium_utils"],
    package_dir={"": "."},
    package_data={"selenium_utils": ["selenium_core.py"]},
    python_requires=">=3.6",
    install_requires=[
        "selenium~=3.0",
        "behave~=1.0",
        "pytest~=6.0",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)