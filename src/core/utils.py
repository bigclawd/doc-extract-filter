#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具函数模块

提供一些通用的工具函数。
"""

import os
from typing import Optional


def get_file_extension(file_path: str) -> Optional[str]:
    """
    获取文件扩展名

    Args:
        file_path: 文件路径

    Returns:
        文件扩展名（小写），如果没有扩展名则返回 None
    """
    ext = os.path.splitext(file_path)[1].lower()
    return ext if ext else None


def is_file_readable(file_path: str) -> bool:
    """
    检查文件是否可读

    Args:
        file_path: 文件路径

    Returns:
        如果文件存在且可读返回 True，否则返回 False
    """
    return os.path.exists(file_path) and os.access(file_path, os.R_OK)
