from setuptools import setup, find_packages
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LONG_DESCRIPTION = BASE_DIR.joinpath('README.md').read_text()


setup(
    name="pyqt5-file-dialogs",
    version="1.0.0",
    description="Interactive file selection prompts using Qt5.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Timothy Pettingill",
    author_email="tpettingill@outlook.com",
    url="https://github.com/timothypettingill/pyqt5-file-dialogs",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["PySide2"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only"

    ]
)