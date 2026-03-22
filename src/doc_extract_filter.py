#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
doc-extract-filter 主模块

提供文本提取和筛选的核心功能，支持 PDF、Word、Excel、TXT 文件。
"""

from typing import Dict, Any, Optional, List
from src.core.extractor import extract_text_from_file
from src.core.filter import filter_text
from src.core.converter import TextConverter


class DocExtractFilter:
    """
    文档提取和筛选类
    
    提供文件文本提取、关键词筛选和格式转换功能。
    """
    
    @staticmethod
    def process(file_path: str, action: str, keywords: Optional[List[str]] = None, 
               regex_pattern: Optional[str] = None) -> Dict[str, Any]:
        """
        处理文件操作
        
        Args:
            file_path: 文件路径
            action: 操作类型，可选 'extract' 或 'filter'
            keywords: 关键词列表（仅 filter 操作需要）
            regex_pattern: 正则表达式模式（仅 filter 操作需要）
            
        Returns:
            包含处理结果的字典
        """
        if action == 'extract':
            return DocExtractFilter.extract(file_path)
        elif action == 'filter':
            return DocExtractFilter.filter(file_path, keywords, regex_pattern)
        else:
            return {
                "success": False,
                "data": {},
                "error": f"不支持的操作类型: {action}"
            }
    
    @staticmethod
    def extract(file_path: str) -> Dict[str, Any]:
        """
        提取文件中的文本
        
        Args:
            file_path: 文件路径
            
        Returns:
            包含提取结果的字典
        """
        return extract_text_from_file(file_path)
    
    @staticmethod
    def filter(file_path: str, keywords: Optional[List[str]] = None, 
               regex_pattern: Optional[str] = None) -> Dict[str, Any]:
        """
        提取文件中的文本并筛选
        
        Args:
            file_path: 文件路径
            keywords: 关键词列表
            regex_pattern: 正则表达式模式
            
        Returns:
            包含筛选结果的字典
        """
        # 先提取文本
        extract_result = extract_text_from_file(file_path)
        if not extract_result["success"]:
            return extract_result
        
        # 然后筛选文本
        text = extract_result["data"]["text"]
        filter_result = filter_text(text, keywords, regex_pattern)
        
        # 合并结果
        result = {
            "success": filter_result["success"],
            "data": {
                "text": text,
                "filtered_text": filter_result["data"].get("filtered_text", "")
            },
            "error": filter_result["error"]
        }
        
        return result
    
    @staticmethod
    def convert_text(text: str, output_format: str, output_file: str, 
                    **kwargs) -> Dict[str, Any]:
        """
        转换文本格式
        
        Args:
            text: 待转换的文本
            output_format: 输出格式，可选 'csv' 或 'xlsx'
            output_file: 输出文件路径
            **kwargs: 其他转换参数
            
        Returns:
            包含转换结果的字典
        """
        converter = TextConverter()
        
        if output_format == 'csv':
            return converter.text_to_csv(text, output_file, **kwargs)
        elif output_format == 'xlsx':
            return converter.text_to_excel(text, output_file, **kwargs)
        else:
            return {
                "status": "error",
                "error": f"不支持的输出格式: {output_format}"
            }
