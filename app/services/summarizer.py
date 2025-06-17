from transformers import pipeline

class TextSummarizer:
    def __init__(self):
        self.model_name = "facebook/bart-large-cnn"
        self.summarizer = pipeline("summarization", model=self.model_name)
                                   
    def summarize(self, text: str, max_length: int = 130, min_length: int = 30) -> str:
        try:
            summary = self.summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )
            return summary[0]['summary_text']
        except Exception as e:
            raise Exception(f"Summarization failed: {str(e)}")