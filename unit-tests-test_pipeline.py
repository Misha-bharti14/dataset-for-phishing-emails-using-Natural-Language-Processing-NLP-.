# tests/test_pipeline.py
import joblib
from phishing_nlp_detection import clean_text

def test_clean_text_basic():
    s = "Hello, this is a test: click http://bad.link"
    cleaned = clean_text(s)
    # Check that the URL is removed and a keyword is retained
    assert "http" not in cleaned
    assert "click" in cleaned

def test_model_saved_and_loadable():
    # Load the artifact created during training
    model = joblib.load('phishing_detector.joblib')
    # Assert that the dictionary contains the two necessary components
    assert 'vectorizer' in model and 'model' in model


