import fitz  # PyMuPDF
import re
import logging
from typing import List, Tuple

logger = logging.getLogger(__name__)

class PDFHandler:
    def __init__(self):
        # 定义敏感词列表或正则表达式模式
        self.sensitive_patterns = [
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # 邮箱
            r'\d{18}|\d{17}[Xx]',  # 身份证
            r'\d{11}',  # 手机号
            # 可以添加更多模式
        ]
        self.compiled_patterns = [re.compile(pattern) for pattern in self.sensitive_patterns]

    def find_sensitive_areas(self, text: str) -> List[Tuple[int, int]]:
        """查找文本中的敏感内容位置"""
        sensitive_areas = []
        for pattern in self.compiled_patterns:
            for match in pattern.finditer(text):
                sensitive_areas.append(match.span())
        return sensitive_areas

    def process_document(self, input_path: str, output_path: str) -> None:
        """处理PDF文档，标记敏感区域"""
        try:
            # 打开PDF文档
            doc = fitz.open(input_path)
            
            for page_num in range(len(doc)):
                page = doc[page_num]
                
                # 获取页面文本
                text = page.get_text()
                
                # 查找敏感区域
                sensitive_areas = self.find_sensitive_areas(text)
                
                for start, end in sensitive_areas:
                    # 获取敏感文本的区域
                    text_instances = page.search_for(text[start:end])
                    
                    # 对每个敏感区域进行标记
                    for inst in text_instances:
                        # 创建黑色矩形覆盖敏感内容
                        page.draw_rect(inst,  # 矩形区域
                                     color=(0, 0, 0),  # 黑色
                                     fill=(0, 0, 0),  # 填充黑色
                                     overlay=True)  # 覆盖原文本
                
                logger.info(f"Processed page {page_num + 1}")
            
            # 保存处理后的文档
            doc.save(output_path)
            doc.close()
            
            logger.info(f"PDF document processed and saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Error processing PDF: {str(e)}")
            raise
