"""
Setup configuration for nepali-num2word package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read version from __init__.py file without importing
def get_version():
    version_file = this_directory / "nepali_num2word" / "__init__.py"
    version_content = version_file.read_text(encoding='utf-8')
    for line in version_content.split('\n'):
        if line.startswith('__version__'):
            return line.split('=')[1].strip().strip('"').strip("'")
    raise RuntimeError("Unable to find version string.")

version = get_version()

setup(
    name="nepali-num2word",
    version=version,
    author="Kushal",
    author_email="kushal.developer@gmail.com", 
    description="Convert numbers to Nepali-style words and formatting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kushal1o1/nepali-num2word",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies - uses only Python standard library
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "nepaliword=cli.main:main",
            "nepaliformat=cli.format_main:main",
            "nepalicompact=cli.compact_main:main",
        ],
    },
    keywords="nepali numbers words conversion currency formatting",
    project_urls={
        "Bug Reports": "https://github.com/kushal1o1/nepali-num2word/issues",
        "Source": "https://github.com/kushal1o1/nepali-num2word",
    },
)