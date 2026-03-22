#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文本提取模块

支持从 PDF、Word、Excel、TXT 格式文件中提取文本内容。
"""

import os
from typing import Dict, Any


def extract_text_from_file(file_path: str) -> Dict[str, Any]:
    """
    从文件中提取文本内容

    Args:
        file_path: 文件路径

    Returns:
        包含提取结果的字典，格式为：
        {
            "success": bool,
            "data": {"text": str},
            "error": str
        }
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            return {
                "success": False,
                "data": {},
                "error": f"文件不存在: {file_path}"
            }

        # 检查文件权限
        if not os.access(file_path, os.R_OK):
            return {
                "success": False,
                "data": {},
                "error": f"权限不足，无法读取文件: {file_path}"
            }

        # 根据文件扩展名调用不同的提取函数
        file_ext = os.path.splitext(file_path)[1].lower()

        if file_ext == ".txt":
            text = _extract_from_txt(file_path)
        elif file_ext == ".pdf":
            text = _extract_from_pdf(file_path)
        elif file_ext == ".docx":
            text = _extract_from_docx(file_path)
        elif file_ext in [".xlsx", ".xls"]:
            text = _extract_from_excel(file_path)
        else:
            return {
                "success": False,
                "data": {},
                "error": f"不支持的文件格式: {file_ext}"
            }

        return {
            "success": True,
            "data": {"text": text},
            "error": ""
        }

    except Exception as e:
        return {
            "success": False,
            "data": {},
            "error": f"提取文本失败: {str(e)}"
        }


def _extract_from_txt(file_path: str) -> str:
    """
    从 TXT 文件中提取文本

    Args:
        file_path: TXT 文件路径

    Returns:
        提取的文本内容
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()


def _extract_from_pdf(file_path: str) -> str:
    """
    从 PDF 文件中提取文本

    Args:
        file_path: PDF 文件路径

    Returns:
        提取的文本内容
    """
    try:
        import PyPDF2
        text = ""
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text
    except ImportError:
        raise Exception("PyPDF2 库未安装，请运行 'pip install PyPDF2'")


def _extract_from_docx(file_path: str) -> str:
    """
    从 Word 文件中提取文本

    Args:
        file_path: Word 文件路径

    Returns:
        提取的文本内容
    """
    try:
        from docx import Document
        doc = Document(file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + '\n'
        return text
    except ImportError:
        raise Exception("python-docx 库未安装，请运行 'pip install python-docx'")


def _extract_from_excel(file_path: str) -> str:
    """
    从 Excel 文件中提取文本

    Args:
        file_path: Excel 文件路径

    Returns:
        提取的文本内容
    """
    try:
        from openpyxl import load_workbook
        wb = load_workbook(file_path)
        text = ""
        for sheet_name in wb.sheetnames:
            sheet = wb[sheet_name]
            text += f"工作表: {sheet_name}\n"
            for row in sheet.iter_rows(values_only=True):
                row_text = '\t'.join([str(cell) if cell is not None else '' for cell in row])
                text += row_text + '\n'
            text += '\n'
        return text
    except ImportError:
        raise Exception("openpyxl 库未安装，请运行 'pip install openpyxl'")
