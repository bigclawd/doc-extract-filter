# doc-extract-filter

文件处理技能，支持 PDF、Word、Excel、TXT 文件的文本提取和关键词筛选。

## 功能特性

- **文本提取**：支持从 PDF、Word、Excel、TXT 格式文件中提取文本内容
- **文本筛选**：支持基于关键词或正则表达式筛选文本内容
- **格式转换**：支持将文本转换为 CSV 或 Excel 格式
- **命令行界面**：提供方便的命令行工具
- **Python API**：提供简洁的 Python 编程接口

## 安装

### 从源码安装

```bash
# 从 GitHub 克隆仓库
git clone https://github.com/bigclawd/doc-extract-filter.git
cd doc-extract-filter

# 或从 Gitee 克隆仓库
git clone https://gitee.com/wang-buhungry/doc-extract-filter.git
cd doc-extract-filter

# 安装依赖
pip install -r requirements.txt

# 安装包
pip install -e .
```

### 依赖项

- Python 3.6+
- PyPDF2 (PDF 文本提取)
- python-docx (Word 文本提取)
- openpyxl (Excel 文本提取)
- click (命令行工具)
- pytest (测试)

## 使用方法

### 命令行使用

```bash
# 提取文本
python cli.py --file_path "path/to/file.pdf" --action "extract"

# 筛选关键词
python cli.py --file_path "path/to/file.pdf" --action "filter" --keywords "关键词1,关键词2"

# 使用正则表达式筛选
python cli.py --file_path "path/to/file.txt" --action "filter" --regex "\d+"
```

### Python API 使用

```python
from src.doc_extract_filter import DocExtractFilter

# 提取文本
result = DocExtractFilter.extract("path/to/file.pdf")
if result["success"]:
    print(result["data"]["text"])
else:
    print(f"错误: {result['error']}")

# 筛选关键词
result = DocExtractFilter.filter("path/to/file.pdf", keywords=["关键词1", "关键词2"])
if result["success"]:
    print(result["data"]["filtered_text"])
else:
    print(f"错误: {result['error']}")

# 使用正则表达式筛选
result = DocExtractFilter.filter("path/to/file.txt", regex_pattern="\d+")
if result["success"]:
    print(result["data"]["filtered_text"])
else:
    print(f"错误: {result['error']}")

# 转换文本格式
result = DocExtractFilter.convert_text("测试文本\n1 2 3", "csv", "output.csv")
if result["status"] == "success":
    print(f"转换成功: {result['output_file']}")
else:
    print(f"错误: {result['error']}")
```

## 项目结构

```
doc-extract-filter/
├── src/                  # 核心业务代码
│   ├── __init__.py       # 包初始化文件
│   ├── doc_extract_filter.py  # 主模块
│   └── core/             # 核心功能模块
│       ├── __init__.py
│       ├── extractor.py  # 文本提取模块
│       ├── filter.py     # 文本筛选模块
│       ├── converter.py  # 格式转换模块
│       └── utils.py      # 工具函数模块
├── tests/                # 单元测试
│   ├── test_extractor.py
│   ├── test_filter.py
│   └── test_doc_extract_filter.py
├── cli.py                # 命令行入口
├── setup.py              # 包安装配置
├── requirements.txt      # 依赖项
├── README.md             # 项目说明
└── .gitignore            # Git 忽略文件
```

## 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_extractor.py

# 运行测试并显示详细信息
pytest -v
```

## 许可证

MIT-0 许可证

## 版本历史

- **1.0.2**：移除了未使用的依赖，优化了项目结构
- **1.0.1**：更新了项目名称和许可证信息
- **1.0.0**：初始版本，实现了基本功能
