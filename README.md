# 文档自动抹除敏感信息

自动检测和标记文档敏感信息的Python程序，支持Word和PDF文档处理。

## 功能特点

- 自动检测文档中的敏感信息
- 支持多种文档格式 (PDF, DOC, DOCX)
- 自动将敏感区域涂黑处理
- 支持自定义敏感信息模式
- 完整的日志记录

## 安装说明

### 1. 克隆项目:
```bash
git clone https://github.com/Lingzilla/document-security-marker.git
cd document-security-marker
```

### 2. 安装 Miniconda (如果未安装):
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

### 3. 创建并激活conda环境:

#### 3.1 可以通过以下命令一键创建环境：

```bash
conda env create -f environment.yml
conda activate doc_security
```

#### 3.2 或者手动创建环境：
##### 3.2.1 创建环境并激活:
```bash
conda create -n doc_security python=3.8
conda activate doc_security
```

##### 3.2.2 安装依赖项:
```bash
conda install -c conda-forge python-docx pymupdf pypdf2 pillow
pip install -r requirements.txt  # 安装其他未在conda中的包
```

## 使用方法

处理PDF文档:
```bash
python main.py input.pdf output.pdf
```

处理Word文档:
```bash
python main.py input.docx output.docx
```

## 项目结构

```
document-security-marker/
├── src/
│   ├── main.py
│   └── document_processor/
│       ├── __init__.py
│       ├── word_handler.py
│       └── pdf_handler.py
├── requirements.txt
└── README.md
```

## 支持的敏感信息类型

- 身份证号码
- 电话号码
- 电子邮箱
- 银行卡号
- 其他自定义模式

## 依赖项

- Python 3.8+
- PyMuPDF
- python-docx
- PyPDF2
- 其他依赖见 requirements.txt