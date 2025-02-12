import unittest
import fitz
import re
import nltk
from collections import Counter
from wordcloud import WordCloud
from nltk.corpus import stopwords
import string
from main import extract_text_from_pdf, clean_text, analyze_pdf, generate_wordcloud


sample_text = "!!This is a sample PDF? text with some common words like the, is, and it. 123!"
nltk.download('stopwords')

available_langs = ["english", "portuguese", "french", "german", "spanish", "italian", "dutch"]
STOPWORDS_CACHE = {lang: set(stopwords.words(lang)) for lang in available_langs}

class TestPDFWordCloud(unittest.TestCase):
    
    def test_extract_text_from_pdf(self):
        """Test that text is extracted correctly from a PDF."""
        pdf_path = "test.pdf"
        text = extract_text_from_pdf(pdf_path)
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)
    
    def test_clean_text(self):
        """Test that text is cleaned correctly, removing punctuation, numbers, and stopwords."""
        lang = "english"
        filtered_words, count = clean_text(sample_text, lang)
        self.assertIsInstance(filtered_words, list)
        self.assertGreater(count, 0)
        
        for word in STOPWORDS_CACHE[lang]:
            self.assertNotIn(word, filtered_words)
        
        for word in filtered_words:
            self.assertFalse(any(char.isdigit() for char in word))
            self.assertFalse(any(char in string.punctuation for char in word))
    
    def test_analyze_pdf(self):
        """Test that PDF analysis returns correct statistics."""
        pdf_path = "test.pdf"
        result = analyze_pdf(pdf_path, "english")
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 6)
   
    def test_generate_wordcloud(self):
        """Test that a word cloud is generated correctly."""
        filtered_words = ["python", "data", "analysis", "science"] * 10
        word_counts = Counter(filtered_words)
        wordcloud = WordCloud().generate_from_frequencies(word_counts)
        self.assertIsInstance(wordcloud, WordCloud)
        self.assertGreater(len(wordcloud.words_), 0)

if __name__ == "__main__":
    unittest.main()
