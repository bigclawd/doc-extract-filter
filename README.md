# doc-extract-filter

文件处理技能，支持 PDF、Word、Excel 文件的文本提取和关键词筛选。

## 功能特性

- **文本提取**：从 PDF、Word、Excel 文件中提取文本内容
- **关键词筛选**：提取文本并筛选包含指定关键词的内容
- **多格式支持**：支持多种文件格式的处理
- **结构化输出**：返回结构化的 JSON 格式结果
- **命令行接口**：提供方便的命令行调用方式
- **Python 函数接口**：支持在 Python 代码中直接调用

## 安装

1. 克隆仓库
   ```bash
   git clone https://gitee.com/wang-buhungry/doc-extract-filter.git
   cd doc-extract-filter
   ```

2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

### 命令行调用

#### 提取文本
```bash
python scripts/doc-extract-filter.py --file_path "path/to/file.pdf" --action "extract"
```

#### 筛选关键词
```bash
python scripts/doc-extract-filter.py --file_path "path/to/file.pdf" --action "filter" --keywords "关键词1,关键词2"
```

### Python 函数调用

```python
from scripts.doc_extract_filter import DocExtractFilter

# 提取文本
result = DocExtractFilter.process("path/to/file.pdf", "extract")

# 筛选关键词
result = DocExtractFilter.process("path/to/file.pdf", "filter", ["关键词1", "关键词2"])
```

## 返回格式

### 成功响应
```json
{
  "success": true,
  "data": {
    "text": "提取的文本内容",
    "filtered_text": "筛选后的文本内容", // 仅 filter 操作返回
    "matches": [ // 仅 filter 操作返回
      {
        "keyword": "关键词1",
        "match": "匹配的文本",
        "context": "上下文内容"
      }
    ],
    "total_matches": 1 // 仅 filter 操作返回
  },
  "error": ""
}
```

### 错误响应
```json
{
  "success": false,
  "data": {},
  "error": "错误信息"
}
```

## 项目结构

```
doc-extract-filter/
├── core/                # 核心功能模块
│   ├── __init__.py
│   ├── converter.py     # 文件格式转换
│   ├── extractor.py     # 文本提取
│   ├── filter.py        # 内容筛选
│   └── utils.py         # 工具函数
├── scripts/             # 脚本文件
│   └── doc-extract-filter.py  # 主脚本
├── LICENSE              # MIT-0 许可证
├── README.md            # 项目说明
├── requirements.txt     # 依赖文件
└── SKILL.md             # 技能配置文件
```

## 支持的文件格式

- **PDF**：使用 pdfplumber 库提取文本
- **Word**：使用 python-docx 库提取文本
- **Excel**：使用 openpyxl 库提取文本

## 错误处理

- 文件不存在：返回错误信息
- 不支持的文件类型：返回错误信息
- 操作失败：返回错误信息

## 许可证

本项目使用 MIT No Attribution License (MIT-0) 许可证。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。
