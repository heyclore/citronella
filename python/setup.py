from setuptools import setup, find_packages
import pathlib


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="citronella",
    version="1.0.0",
    license="MIT",
    description="Webdriver Extension with Page Object Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/heyclore/citronella/tree/main/python#readme",
    author="heyclore",
    author_email="cloore@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="test, unittest, pytest, webdriver, appium, selenium",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires="~=3.7",
    install_requires=["selenium"],
    project_urls={
        "Source": "https://github.com/heyclore/citronella/tree/main/python",
    },
)
