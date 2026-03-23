#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文本筛选模块

基于关键词或正则表达式筛选文本内容，支持排除筛选。
"""

import re
from typing import Dict, Any, Optional, List


def filter_text(text: str, keywords: Optional[List[str]] = None, 
               regex_pattern: Optional[str] = None, exclude_keywords: Optional[List[str]] = None,
               exclude_regex: Optional[str] = None, context_length: int = 50, 
               filter_level: str = "line") -> Dict[str, Any]:
    """
    基于关键词或正则表达式筛选文本

    Args:
        text: 待筛选的文本
        keywords: 关键词列表
        regex_pattern: 正则表达式模式
        exclude_keywords: 排除关键词列表
        exclude_regex: 排除正则表达式模式
        context_length: 上下文长度（默认50字符）
        filter_level: 筛选级别，line（按行）或 paragraph（按段落）

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
            # 按行或段落分割文本
            if filter_level == "line":
                segments = text.split('\n')
            else:  # paragraph
                segments = text.split('\n\n')
                
            for keyword in keywords:
                for i, segment in enumerate(segments):
                    if keyword in segment:
                        # 提取上下文
                        context = _get_context(segments, i, context_length, filter_level)
                        # 检查是否需要排除（检查整个上下文）
                        if not _should_exclude(context, exclude_keywords, exclude_regex):
                            filtered_text += f"关键词: {keyword}\n"
                            filtered_text += f"匹配内容:\n{context}\n"
                            filtered_text += "-" * 80 + "\n"

        # 基于正则表达式筛选
        elif regex_pattern:
            # 按行或段落分割文本
            if filter_level == "line":
                segments = text.split('\n')
            else:  # paragraph
                segments = text.split('\n\n')
                
            for i, segment in enumerate(segments):
                if re.search(regex_pattern, segment, re.MULTILINE | re.DOTALL):
                    # 提取上下文
                    context = _get_context(segments, i, context_length, filter_level)
                    # 检查是否需要排除（检查整个上下文）
                    if not _should_exclude(context, exclude_keywords, exclude_regex):
                        filtered_text += f"正则匹配: {regex_pattern}\n"
                        filtered_text += f"匹配内容:\n{context}\n"
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


def _should_exclude(text: str, exclude_keywords: Optional[List[str]], 
                   exclude_regex: Optional[str]) -> bool:
    """
    检查文本是否应该被排除

    Args:
        text: 待检查的文本
        exclude_keywords: 排除关键词列表
        exclude_regex: 排除正则表达式模式

    Returns:
        是否应该被排除
    """
    # 检查排除关键词
    if exclude_keywords:
        for keyword in exclude_keywords:
            if keyword in text:
                return True
    
    # 检查排除正则表达式
    if exclude_regex:
        if re.search(exclude_regex, text, re.MULTILINE | re.DOTALL):
            return True
    
    return False


def _get_context(segments: List[str], index: int, context_length: int, 
                filter_level: str) -> str:
    """
    获取匹配内容的上下文

    Args:
        segments: 文本段列表
        index: 匹配段的索引
        context_length: 上下文长度
        filter_level: 筛选级别

    Returns:
        包含上下文的文本
    """
    # 计算上下文范围
    start = max(0, index - 1)
    end = min(len(segments), index + 2)
    
    # 提取上下文
    context_segments = segments[start:end]
    
    # 连接上下文
    if filter_level == "line":
        context = '\n'.join(context_segments)
    else:  # paragraph
        context = '\n\n'.join(context_segments)
    
    # 限制上下文长度
    if len(context) > context_length:
        # 找到匹配段在上下文中的位置
        match_start = context.find(segments[index])
        if match_start == -1:
            match_start = 0
        
        # 计算上下文的起始和结束位置
        context_start = max(0, match_start - context_length // 2)
        context_end = min(len(context), match_start + len(segments[index]) + context_length // 2)
        
        # 截取上下文
        context = context[context_start:context_end]
        if context_start > 0:
            context = "..." + context
        if context_end < len(context):
            context = context + "..."
    
    return context
