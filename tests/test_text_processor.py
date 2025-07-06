import pytest
from scripts.text_processor import ProcessText

@pytest.fixture
def processor():
    return ProcessText(chunk_size=20, chunk_overlap=5, separators=[" ", "\n"])

def test_prepare_text_removes_boilerplate(processor):
    text = "I am writing to file a complaint regarding my credit card. The issue is unresolved."
    cleaned = processor.prepare_text(text)
    assert "i am writing to file a complaint regarding" not in cleaned
    assert "credit card" in cleaned
    assert cleaned == "my credit card the issue is unresolved"

def test_prepare_text_removes_special_characters_and_numbers(processor):
    text = "Account #12345! This is a complaint regarding $1000."
    cleaned = processor.prepare_text(text)
    assert "#" not in cleaned
    assert "$" not in cleaned
    assert "12345" not in cleaned
    assert "1000" not in cleaned
    assert cleaned == "account this is a complaint regarding"

def test_prepare_text_lowercases_and_normalizes_whitespace(processor):
    text = "   To Whom It May Concern:   \n\nThis is a TEST.   "
    cleaned = processor.prepare_text(text)
    assert cleaned == "this is a test"

def test_split_chunks_text(processor):
    text = "This is a long complaint text that should be split into several chunks for processing."
    chunks = processor.split(text)
    # With chunk_size=20 and chunk_overlap=5, expect multiple chunks
    assert isinstance(chunks, list)
    assert all(isinstance(chunk, str) for chunk in chunks)
    assert len(chunks) > 1

def test_run_all_combines_prepare_and_split(processor):
    text = "I would like to file a complaint about my loan. The lender is not responding."
    chunks = processor.run_all(text)
    # Should remove boilerplate and split the cleaned text
    assert isinstance(chunks, list)
    assert all(isinstance(chunk, str) for chunk in chunks)
    # Check that boilerplate is removed in all chunks
    assert all("i would like to file a complaint" not in chunk for chunk in chunks)
    # Check that relevant content remains
    assert any("loan" in chunk for chunk in chunks)