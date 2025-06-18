import pytest
from services.summarizer import TextSummarizer

def test_summarizer_initialization():
    summerizer = TextSummarizer()
    assert summerizer is not None
    assert summerizer.model_name == "sshleifer/distilbart-cnn-12-6"

def test_summarizer_short_text():
    summerizer = TextSummarizer()
    with pytest.raises(ValueError):
        summerizer.summarize("Short text")

def test_summarizer_normal_test():
    summarizer = TextSummarizer()
    text = "Your long test text here..." * 10
    summary = summarizer.summarize(text)
    assert isinstance(summary, str)
    assert len(summary) < len(text)