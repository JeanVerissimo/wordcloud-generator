# PDF WordCloud Generator

## Overview

This project implements a **PDF WordCloud Generator** that extracts text from a PDF file, processes it by removing stopwords, numbers, and punctuation, and generates a word cloud based on word frequency analysis.

### Key Features:
- **Stopword Removal**: Cleans the extracted text by removing stopwords based on the selected language.
- **Word Frequency Analysis**: Calculates word occurrences and highlights the most frequently used words.
- **Word Cloud Generation**: Displays a visually appealing word cloud using the `wordcloud` and `matplotlib` libraries.
- **Multi-language Support**: Supports stopword removal in multiple languages.

---

## Installation

To run this project, ensure you have Python 3.x installed. Additionally, you will need to install the required dependencies.

1. **Clone the repository**:

```bash
git clone https://github.com/JeanVerissimo/pdf-wordcloud-generator.git
cd pdf-wordcloud-generator
```

2. **Install dependencies**:

```bash
pip install pymupdf nltk wordcloud matplotlib
```

3. **Download NLTK stopwords**:

```python
import nltk
nltk.download('stopwords')
```

---

## Usage

Run the `pdf_wordcloud.py` script to start the application. This script provides a **GUI interface** to select a PDF file, analyze its content, and generate a word cloud.

```bash
python pdf_wordcloud.py
```

### Steps to Use:
1. **Select Language**: Choose a language from the dropdown menu.
2. **Load PDF**: Click the "Load PDF" button to select a file.
3. **View Word Statistics**: The extracted text is analyzed, and key statistics such as total words, unique words, and word frequency are displayed.
4. **Generate Word Cloud**: Click the "Generate WordCloud" button to visualize the most frequent words.

---
