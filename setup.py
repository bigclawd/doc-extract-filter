#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
doc-extract-filter 包安装配置文件
"""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    install_requires = [line.strip() for line in f if line.strip()]

setup(
    name="doc-extract-filter",
    version="1.0.2",
    author="file-agent team",
    author_email="",
    description="文件处理技能，支持 PDF、Word、Excel 文件的文本提取和关键词筛选",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/wang-buhungry/doc-extract-filter",
    project_urls={
        "GitHub": "https://github.com/bigclawd/doc-extract-filter",
        "Gitee": "https://gitee.com/wang-buhungry/doc-extract-filter",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "doc-extract-filter=cli:main",
        ],
    },
)
