from setuptools import setup, find_packages
import pathlib


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="citronella",
    version="0.0.0",
    description="a selenium extension for page object model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/heyclore/citronella",
    author="heyclore",
    author_email="cloore@gmail.com",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="test, unittest",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3, < 4",
    install_requires=["selenium"],
    project_urls={
        "Source": "https://github.com/heyclore/citronella",
    },
)
