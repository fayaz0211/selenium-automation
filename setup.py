import sys

from setuptools import setup

assert sys.version_info >= (3, 6, 0), "selenium-utils_auth requires Python 3.6+"
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta

setup(
    name="selenium-utils",
    description="A python library to add selenium utils to apps",
    url="https://github.com/fayaz0211/selenium-automation/tree/main/selenium_utils",
    license="MIT",
    packages=["selenium-utils"],
    package_dir={"": "."},
    package_data={"selenium-utils": ["py.typed"]},
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