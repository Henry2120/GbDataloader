from setuptools import setup, find_packages

setup(
    name="garbagedataloader",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",  # Add other dependencies as needed
    ],
    author="Dat Nguyen Van",
    author_email="",
    description="Garbage Dataloader is a library installed to facilitate the quick download and loading of data for researchers, allowing them to access this data as swiftly as possible.",
    long_description="Garbage Dataloader is a compilation of four publicly available datasets that we used in our paper, including Bataci's dataset, AndroVul dataset, Drebin-215 dataset, Malgenome-215 dataset, and a feature dataset collected by our proposed framework (which includes CSV files and sha256 hashes).",
    long_description_content_type="text/markdown",
    url="https://github.com/Henry2120/GbDataloader.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
