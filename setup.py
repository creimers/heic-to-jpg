#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "Click>=7.0",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Christoph Reimers",
    author_email="christoph@superservice-international.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Convert .heic images to .jpg",
    entry_points={
        "console_scripts": [
            "heic2jpg = heic_to_jpg.cli:main",
            "heic-to-jpg = heic_to_jpg.cli:main",
        ]
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="heic_to_jpg",
    name="heic_to_jpg",
    py_modules=["heic_to_jpg"],
    packages=find_packages(include=["heic_to_jpg", "heic_to_jpg.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/creimers/heic-to-jpg",
    version="0.1.8",
    zip_safe=False,
)
