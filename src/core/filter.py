#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文本筛选模块

基于关键词或正则表达式筛选文本内容。
"""

import re
from typing import Dict, Any, Optional, List


def filter_text(text: str, keywords: Optional[List[str]] = None, 
               regex_pattern: Optional[str] = None) -> Dict[str, Any]:
    """
    基于关键词或正则表达式筛选文本

    Args:
        text: 待筛选的文本
        keywords: 关键词列表
        regex_pattern: 正则表达式模式

    Returns:
        包含筛选结果的字典，格式为：
        {
            "success": bool,
            "data": {"filtered_text": str},
            "error": str
        }
    """
    try:
        filtered_text = ""

        # 基于关键词筛选
        if keywords:
            for keyword in keywords:
                if keyword in text:
                    # 提取包含关键词的上下文
                    lines = text.split('\n')
                    for i, line in enumerate(lines):
                        if keyword in line:
                            # 包含前后各2行上下文
                            start = max(0, i - 2)
                            end = min(len(lines), i + 3)
                            context = '\n'.join(lines[start:end])
                            filtered_text += f"关键词: {keyword}\n"
                            filtered_text += f"匹配内容:\n{context}\n"
                            filtered_text += "-" * 80 + "\n"

        # 基于正则表达式筛选
        elif regex_pattern:
            matches = re.findall(regex_pattern, text, re.MULTILINE | re.DOTALL)
            for i, match in enumerate(matches):
                filtered_text += f"匹配 #{i+1}:\n{match}\n"
                filtered_text += "-" * 80 + "\n"

        else:
            return {
                "success": False,
                "data": {},
                "error": "请提供关键词或正则表达式"
            }

        if not filtered_text:
            filtered_text = "未找到匹配内容"

        return {
            "success": True,
            "data": {"filtered_text": filtered_text},
            "error": ""
        }

    except Exception as e:
        return {
            "success": False,
            "data": {},
            "error": f"筛选文本失败: {str(e)}"
        }
