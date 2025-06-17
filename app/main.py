from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.summarizer import TextSummarizer
from app.utils.text_cleaner import TextCleaner

app = FastAPI(title="Text Summarizer API")
summarizer = TextSummarizer()
cleaner = TextCleaner()

class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 130
    min_length: int = 30

@app.post("/summarize")
async def summarize_text(request: SummarizeRequest):
    try:
        if not cleaner.validate_text(request.text):
            raise HTTPException(status_code=400, detail="Invalid text input")
        
        cleaned_text = cleaner.clean_text(request.text)
        summary = summarizer.summarize(
            cleaned_text,
            request.max_length,
            request.min_length
        )

        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))