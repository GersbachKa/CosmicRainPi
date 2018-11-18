import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cosmicrain",
    version="0.5.1",
    author="Kyle Gersbach",
    author_email="Gersbach.ka@gmail.com",
    description="Playing modulated music with cosmic rays!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GersbachKa/CosmicRainPi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)