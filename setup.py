import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mostpopularnewscnnid",
    version="0.0.1",
    author="Tri Prasetyo Kusumo Aji",
    author_email="ajikprasetyo22@gmail.com",
    description="This package will get the most popular news in CNN Indonesia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jetkesuma/most-popular-news-cnn-id",
    project_urls={
        "Medium": "https://medium.com/@kusumo999666",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPlv3)",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
