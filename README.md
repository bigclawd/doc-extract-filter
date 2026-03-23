# doc-extract-filter

文件处理技能，支持多种文件格式的文本提取、关键词/正则表达式筛选、排除筛选和批量文件处理。

## 功能特性

- **文本提取**：支持从 PDF、Word、Excel、TXT、CSV、Markdown、WPS 格式文件中提取文本内容
- **文本筛选**：支持基于关键词或正则表达式筛选文本内容，支持排除筛选
- **OCR 支持**：支持扫描件 PDF 的轻量 OCR 提取
- **智能格式检测**：自动识别文件类型，无需用户指定
- **批量处理**：支持批量处理多个文件，支持文件夹遍历和多文件列表
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
- tqdm (进度条)
- python-markdown (Markdown 文件处理)
- beautifulsoup4 (HTML 文本提取)
- pytest (测试)
- 可选依赖：pytesseract、pdf2image、Pillow (OCR 功能)

## 使用方法

### 命令行使用

```bash
# 提取文本
python cli.py --file_path "path/to/file.pdf" --action "extract"

# 提取 PDF 扫描件（启用 OCR）
python cli.py --file_path "path/to/scanned.pdf" --action "extract" --enable-ocr

# 筛选关键词
python cli.py --file_path "path/to/file.pdf" --action "filter" --keywords "关键词1,关键词2"

# 筛选并排除指定内容
python cli.py --file_path "path/to/file.pdf" --action "filter" --keywords "关键词" --exclude-keywords "排除词"

# 使用正则表达式筛选
python cli.py --file_path "path/to/file.txt" --action "filter" --regex "\d+"

# 设置上下文长度和筛选级别
python cli.py --file_path "path/to/file.txt" --action "filter" --keywords "关键词" --context-length 100 --filter-level "paragraph"

# 批量处理 - 文件夹路径
python cli.py --batch --input-dir "path/to/folder" --action "extract" --output-dir "batch-results"

# 批量处理 - 文件列表
python cli.py --batch --file-paths "path/to/file1.pdf,path/to/file2.docx" --action "extract" --output-dir "batch-results"

# 批量处理并合并结果
python cli.py --batch --input-dir "path/to/folder" --action "extract" --output-dir "batch-results" --merge-results

# 批量筛选
python cli.py --batch --input-dir "path/to/folder" --action "filter" --keywords "关键词" --output-dir "batch-results"
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

# 提取 PDF 扫描件（启用 OCR）
result = DocExtractFilter.extract("path/to/scanned.pdf", enable_ocr=True)
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

# 筛选并排除指定内容
result = DocExtractFilter.filter("path/to/file.pdf", keywords=["关键词"], exclude_keywords=["排除词"])
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

# 批量处理
result = DocExtractFilter.batch_process(
    input_dir="path/to/folder",
    action="extract",
    output_dir="batch-results"
)
if result["success"]:
    print(f"批量处理成功，处理了 {result['data']['summary']['total_files']} 个文件")
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
├── doc-extract-filter-skill/  # 技能配置文件夹
│   ├── core/             # 技能核心代码
│   ├── scripts/          # 技能脚本
│   ├── SKILL.md          # 技能配置文件
│   └── requirements.txt  # 技能依赖
├── tests/                # 单元测试
│   ├── test_extractor.py
│   ├── test_filter.py
│   ├── test_doc_extract_filter.py
│   ├── test_batch_process.py
│   ├── test_compatibility.py
│   └── test_filter_enhance.py
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

# 运行兼容性测试
pytest tests/test_compatibility.py

# 运行筛选增强测试
pytest tests/test_filter_enhance.py
```

## 许可证

MIT-0 许可证

## 版本历史

- **1.1.1**：新增格式扩展+兼容性优化和筛选功能增强
  - 新增支持 CSV、Markdown（.md）、WPS（.wps/.et）文件提取
  - 修复 Excel 合并单元格、PDF 扫描件、Word 图文混排的提取问题
  - 新增 --enable-ocr 参数（可选），支持扫描件 PDF 轻量 OCR 提取
  - 新增智能格式检测逻辑，自动识别文件类型，无需用户指定
  - 新增 --exclude-keywords/--exclude-regex 参数，支持排除指定内容
  - 新增 --context-length N 参数，返回筛选结果的上下文（默认 50 字符）
  - 新增 --filter-level（line/paragraph）参数，支持按行/段落筛选
  - 批量处理模式下，筛选增强逻辑自动适配，结果按文件维度保留筛选细节
  - 依赖新增 tesseract（可选）、python-markdown，写入 requirements.txt 并标注可选
- **1.1.0**：添加了批量文件处理功能
- **1.0.3**：添加了正则表达式筛选功能
- **1.0.2**：移除了未使用的依赖，优化了项目结构
- **1.0.1**：更新了项目名称和许可证信息
- **1.0.0**：初始版本，实现了基本功能