# Author: MORIKI Ginga <gingiragin@outlook.jp>
# Copyright (c) 2023- MORIKI Ginga
# Licence: MIT

from setuptools import setup

DESCRIPTION = "jsonkeysearch: Searches for keys in JSON format files."
NAME = "jsonkeysearch"
AUTHOR = "TAKAHASHI Taro"
AUTHOR_EMAIL = "gingiragin@outlook.jp"
URL = "https://github.com/gmoriki/jsonkeysearch"
LICENSE = "MIT"
DOWNLOAD_URL = URL
VERSION = "0.1.0"
PYTHON_REQUIRES = ">=3.6"
INSTALL_REQUIRES = ["pytz>=2020.1"]
PACKAGES = ["jsonkeysearch"]
KEYWORDS = "json search"
CLASSIFIERS = ["License :: OSI Approved :: MIT License", "Programming Language :: Python :: 3.10"]
with open("README.md", "r", encoding="utf-8") as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES,
)
