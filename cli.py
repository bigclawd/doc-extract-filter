#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
doc-extract-filter - 文件处理技能封装脚本

支持 PDF、Word、Excel 文件的文本提取和关键词筛选
适配 OpenClaw 和 CoPaw 智能体调用规范
"""

import os
import sys
import json
import logging
import click
from pathlib import Path

# 添加当前目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent))

from src.core.extractor import extract_text_from_file
from src.core.filter import filter_text

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DocExtractFilter:
    """
    文件处理技能类
    """
    
    @staticmethod
    def process(file_path, action, keywords=None, regex_pattern=None):
        """
        处理文件操作
        
        Args:
            file_path: 文件路径
            action: 操作类型，extract 或 filter
            keywords: 关键词列表，仅 filter 操作需要
            regex_pattern: 正则表达式模式，仅 filter 操作需要
            
        Returns:
            结构化 JSON 格式的结果
        """
        try:
            # 验证文件路径
            file_path = Path(file_path)
            if not file_path.exists():
                return {
                    "success": False,
                    "data": {},
                    "error": f"文件不存在: {file_path}"
                }
            
            # 提取文本
            extract_result = extract_text_from_file(file_path)
            
            if not extract_result["success"]:
                return extract_result
            
            text = extract_result.get("data", {}).get("text", "")
            
            # 根据操作类型处理
            if action == "extract":
                return {
                    "success": True,
                    "data": {
                        "text": text
                    },
                    "error": ""
                }
            elif action == "filter":
                if not keywords and not regex_pattern:
                    return {
                        "success": False,
                        "data": {},
                        "error": "filter 操作需要提供关键词或正则表达式"
                    }
                
                # 筛选关键词或正则表达式
                filter_result = filter_text(text, keywords, regex_pattern)
                
                if not filter_result["success"]:
                    return filter_result
                
                # 构建筛选后的文本
                filtered_text = filter_result.get("data", {}).get("filtered_text", "")
                
                return {
                    "success": True,
                    "data": {
                        "text": text,
                        "filtered_text": filtered_text
                    },
                    "error": ""
                }
            else:
                return {
                    "success": False,
                    "data": {},
                    "error": f"不支持的操作类型: {action}"
                }
                
        except Exception as e:
            logger.error(f"处理文件时出错: {str(e)}")
            return {
                "success": False,
                "data": {},
                "error": str(e)
            }


@click.command()
@click.option('--file_path', required=True, help='文件路径')
@click.option('--action', required=True, type=click.Choice(['extract', 'filter']), help='操作类型')
@click.option('--keywords', help='关键词列表，逗号分隔')
@click.option('--regex', help='正则表达式模式')
def cli(file_path, action, keywords, regex):
    """
    命令行接口
    """
    # 处理关键词参数
    keyword_list = []
    if keywords:
        keyword_list = [k.strip() for k in keywords.split(',')]
    
    # 调用处理函数
    result = DocExtractFilter.process(file_path, action, keyword_list, regex)
    
    # 输出 JSON 格式结果
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    cli()
