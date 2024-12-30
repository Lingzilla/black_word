import argparse
import logging
import os
from pathlib import Path
from document_processor.word_handler import WordHandler
from document_processor.pdf_handler import PDFHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentProcessor:
    def __init__(self):
        self.word_handler = WordHandler()
        self.pdf_handler = PDFHandler()

    def process_file(self, input_path: str, output_path: str) -> None:
        """
        Process input document and mark sensitive areas
        
        Args:
            input_path: Path to input document
            output_path: Path to save processed document
        """
        file_extension = Path(input_path).suffix.lower()
        
        try:
            if file_extension in ['.doc', '.docx']:
                self.word_handler.process_document(input_path, output_path)
            elif file_extension == '.pdf':
                self.pdf_handler.process_document(input_path, output_path)
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
            
            logger.info(f"Successfully processed {input_path}")
            
        except Exception as e:
            logger.error(f"Error processing file {input_path}: {str(e)}")
            raise

def main():
    parser = argparse.ArgumentParser(description='Document Security Marker')
    parser.add_argument('input_file', help='Path to input document (PDF or Word)')
    parser.add_argument('output_file', help='Path to save processed document')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        logger.error(f"Input file not found: {args.input_file}")
        return
    
    try:
        processor = DocumentProcessor()
        processor.process_file(args.input_file, args.output_file)
        logger.info("Document processing completed successfully")
        
    except Exception as e:
        logger.error(f"Processing failed: {str(e)}")
        return

if __name__ == "__main__":
    main()