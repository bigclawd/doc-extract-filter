# doc-extract-filter

## 元数据

### 基本信息
- **name**: doc-extract-filter
- **description**: 文件处理技能，支持 PDF、Word、Excel 文件的文本提取、关键词/正则表达式筛选和批量文件处理
- **version**: 1.1.0
- **author**: file-agent team
- **license**: MIT-0

### OpenClaw 配置
```json
{
  "name": "doc-extract-filter",
  "description": "文件处理技能，支持 PDF、Word、Excel 文件的文本提取、关键词/正则表达式筛选和批量文件处理",
  "version": "1.1.0",
  "author": "file-agent team",
  "license": "MIT-0",
  "type": "tool",
  "entry_point": "scripts/doc-extract-filter.py",
  "parameters": {
    "file_path": {
      "type": "string",
      "description": "文件路径",
      "required": false
    },
    "action": {
      "type": "string",
      "description": "操作类型：extract 或 filter",
      "required": true
    },
    "keywords": {
      "type": "array",
      "description": "关键词列表（仅 filter 操作需要）",
      "required": false
    },
    "regex": {
      "type": "string",
      "description": "正则表达式模式（仅 filter 操作需要）",
      "required": false
    },
    "batch": {
      "type": "boolean",
      "description": "开启批量处理模式",
      "required": false
    },
    "input_dir": {
      "type": "string",
      "description": "批量处理的输入文件夹路径",
      "required": false
    },
    "file_paths": {
      "type": "array",
      "description": "批量处理的文件列表",
      "required": false
    },
    "output_dir": {
      "type": "string",
      "description": "批量结果输出目录",
      "required": false
    },
    "merge_results": {
      "type": "boolean",
      "description": "是否合并所有文件结果为一个 JSON 文件",
      "required": false
    }
  }
}
```

### CoPaw 配置
```yaml
name: doc-extract-filter
description: 文件处理技能，支持 PDF、Word、Excel 文件的文本提取、关键词/正则表达式筛选和批量文件处理
version: 1.1.0
author: file-agent team
license: MIT-0
type: tool
entry_point: scripts/doc-extract-filter.py
parameters:
  file_path:
    type: string
    description: 文件路径
    required: false
  action:
    type: string
    description: 操作类型：extract 或 filter
    required: true
  keywords:
    type: array
    description: 关键词列表（仅 filter 操作需要）
    required: false
  regex:
    type: string
    description: 正则表达式模式（仅 filter 操作需要）
    required: false
  batch:
    type: boolean
    description: 开启批量处理模式
    required: false
  input_dir:
    type: string
    description: 批量处理的输入文件夹路径
    required: false
  file_paths:
    type: array
    description: 批量处理的文件列表
    required: false
  output_dir:
    type: string
    description: 批量结果输出目录
    required: false
  merge_results:
    type: boolean
    description: 是否合并所有文件结果为一个 JSON 文件
    required: false
```

## 更新说明
- **版本 1.1.0**: 添加了批量文件处理功能
- **版本 1.0.3**: 添加了正则表达式筛选功能
- **版本 1.0.2**: 移除了未使用的依赖，优化了项目结构

## 使用说明

### 功能
- **extract**: 提取文件中的文本内容
- **filter**: 提取文件中的文本并筛选包含指定关键词或匹配正则表达式的内容
- **batch**: 批量处理多个文件，支持文件夹遍历和多文件列表

### 调用方式

#### CLI 调用
```bash
# 单个文件处理
python scripts/doc-extract-filter.py --file_path "path/to/file.pdf" --action "extract"
python scripts/doc-extract-filter.py --file_path "path/to/file.pdf" --action "filter" --keywords "关键词1,关键词2"
python scripts/doc-extract-filter.py --file_path "path/to/file.pdf" --action "filter" --regex "\\d{4}-\\d{2}-\\d{2}"

# 批量处理 - 文件夹路径
python scripts/doc-extract-filter.py --batch --input-dir "path/to/folder" --action "extract" --output-dir "batch-results"

# 批量处理 - 文件列表
python scripts/doc-extract-filter.py --batch --file-paths "path/to/file1.pdf,path/to/file2.docx" --action "extract" --output-dir "batch-results"

# 批量处理并合并结果
python scripts/doc-extract-filter.py --batch --input-dir "path/to/folder" --action "extract" --output-dir "batch-results" --merge-results

# 批量筛选
python scripts/doc-extract-filter.py --batch --input-dir "path/to/folder" --action "filter" --keywords "关键词" --output-dir "batch-results"
```

#### Python 函数调用
```python
from scripts.doc_extract_filter import DocExtractFilter

# 提取文本
result = DocExtractFilter.process("path/to/file.pdf", "extract")

# 筛选关键词
result = DocExtractFilter.process("path/to/file.pdf", "filter", ["关键词1", "关键词2"])

# 使用正则表达式筛选
result = DocExtractFilter.process("path/to/file.pdf", "filter", regex_pattern="\\d{4}-\\d{2}-\\d{2}")

# 批量处理 - 文件夹路径
result = DocExtractFilter.batch_process(
    input_dir="path/to/folder",
    action="extract",
    output_dir="batch-results"
)

# 批量处理 - 文件列表
result = DocExtractFilter.batch_process(
    file_paths=["path/to/file1.pdf", "path/to/file2.docx"],
    action="extract",
    output_dir="batch-results"
)

# 批量处理并合并结果
result = DocExtractFilter.batch_process(
    input_dir="path/to/folder",
    action="extract",
    output_dir="batch-results",
    merge_results=True
)
```

### 返回格式
```json
{
  "success": true,
  "data": {
    "text": "提取的文本内容",
    "filtered_text": "筛选后的文本内容" // 仅 filter 操作返回
  },
  "error": ""
}
```

### 错误处理
- 文件不存在：返回错误信息
- 不支持的文件类型：返回错误信息
- 操作失败：返回错误信息

## 安装与测试

### 安装
1. 将 `doc-extract-filter` 目录复制到 OpenClaw/CoPaw 的 skills 目录
2. 运行 `pip install -r requirements.txt` 安装依赖

### 测试
使用 `docs/test.pdf` 文件测试功能：
```bash
# 测试提取文本
python scripts/doc-extract-filter.py --file_path "docs/test.pdf" --action "extract"

# 测试关键词筛选
python scripts/doc-extract-filter.py --file_path "docs/test.pdf" --action "filter" --keywords "单价,小计,总金额"
```

### 独立运行
doc-extract-filter 现在包含了所有必要的核心代码，可以独立运行，不依赖于外部的 src 目录。