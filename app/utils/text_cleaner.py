import re

class TextCleaner:
    @staticmethod
    def clean_text(text: str) -> str:
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s.,!?-]', '', text)
        return text.strip()
    
    @staticmethod
    def validate_text(text: str) -> bool:
        if not text or len(text.strip()) < 100:
            return False
        return True