import setuptools

import os

print("Path: ", os.getcwd())

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smartprint",
    version="0.1.2",
    author="abcnishant007, nickdelgrosso",
    author_email="abc.nishant007@gmail.com",
    description="Include the variable name in print statements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abcnishant007/smartprint",
    project_urls={
        "Bug Tracker": "https://github.com/abcnishant007/smartprint/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
