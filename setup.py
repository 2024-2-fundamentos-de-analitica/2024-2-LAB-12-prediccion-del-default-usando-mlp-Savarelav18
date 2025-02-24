"""Package installer"""

from setuptools import find_packages, setup  # type: ignore

setup(
    name="homework",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "pandas",
        "scikit-learn",
        "numpy == 2.1.0",
        "ipykernel",
        "xlrd",
    ],
)
