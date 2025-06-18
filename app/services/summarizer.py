from transformers import pipeline
import torch
from typing import Optional

class TextSummarizer:
    model_name = "sshleifer/distilbart-cnn-12-6"

    def __init__(self, model_name: Optional[str] = None):
        if model_name:
            self.model_name = model_name

        try:
            self.summarizer = pipeline("summarization", model=self.model_name)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize the model: {str(e)}")
                                   
    def summarize(self, 
                 text: str, 
                 max_length: int = 130, 
                 min_length: int = 30,
                 do_sample: bool = True,
                 num_beams: int = 4,
                 temperature: float = 0.7
                 ) -> str:
        try:
            if not text or len(text.strip()) < min_length:
                raise ValueError("Input text is too short or empty")

            summary = self.summarizer(text,
                                    max_length=max_length,
                                    min_length=min_length,
                                    do_sample=do_sample,
                                    num_beams=num_beams,
                                    temperature=temperature
                                    )
            
            return summary[0]['summary_text'] if summary else "No summary generated"
        except ValueError as e:
            raise e
        except Exception as e:
            raise RuntimeError(f"Summarization failed: {str(e)}")