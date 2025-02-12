import fitz
import re
import nltk
import tkinter as tk
from tkinter import filedialog, ttk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from collections import Counter

stored_words = []
available_langs = ["english", "portuguese", "french", "german", "spanish", "italian", "dutch"]
nltk.download('stopwords')
STOPWORDS_CACHE = {lang: set(stopwords.words(lang)) for lang in available_langs}

root = tk.Tk()
root.title("PDF WordCloud Generator")

#Language selection
language_var = tk.StringVar(value=available_langs[0])
tk.Label(root, text="Select Language:").pack()
lang_dropdown = ttk.Combobox(root, textvariable=language_var, values=available_langs, state="readonly")
lang_dropdown.pack()

# Table to display PDF info
table_data = tk.Variable(value=[])
columns = ("Number of Pages", "Total Words", "Words Without Stopwords", "Avg Words/Page", "Unique Words")
treeview = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    treeview.heading(col, text=col)
treeview.pack()

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text("text") + " "
    
    if not text.strip():
        return "No text found in this PDF."
    
    return text


def clean_text(text, lang):
    text = re.sub(r'[^\w\s]', '', text)     # Remove punctuation
    text = re.sub(r'\d+', '', text)         # Remove numbers
    text = text.lower()
    words = text.split()
    stop_words = STOPWORDS_CACHE.get(lang, set())
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words, len(filtered_words)

def analyze_pdf(pdf_path, lang):
    text = extract_text_from_pdf(pdf_path)
    num_pages = len(fitz.open(pdf_path))
    num_words = len(text.split())
    filtered_words, num_filtered_words = clean_text(text, lang)
    avg_words_per_page = round(num_words / num_pages, 2) if num_pages > 0 else 0
    unique_words = len(set(filtered_words))
    return num_pages, num_words, num_filtered_words, avg_words_per_page, unique_words, filtered_words


def generate_wordcloud(filtered_words):
    word_counts = Counter(filtered_words)
    top_words = word_counts.most_common(5)
    
    wordcloud = WordCloud(width=1000, height=1000, background_color='white', colormap='coolwarm').generate_from_frequencies(word_counts)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    legend_text = "\n".join([f"{word}: {count} times." for word, count in top_words])
    plt.figtext(0.15, 0.05, legend_text, fontsize=12, bbox={"facecolor": "white", "alpha": 0.5, "pad": 5})
    plt.show()


def load_pdf():
    #Clean the table
    for row in treeview.get_children():
        treeview.delete(row)

    lang = language_var.get()
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    
    if not file_path:  # If no file was selected, show a message and return
        loading_label.config(text="No file selected.")
        return

    try:
        result = analyze_pdf(file_path, lang)
    except Exception as error_msg:
        loading_label.config(text=f"Error processing PDF: {str(error_msg)}")
        return
    
    if result is None:
        loading_label.config(text="Error: File processing failed.")
        return
    
    num_pages, num_words, num_filtered_words, avg_words_per_page, unique_words, filtered_words = result
    treeview.insert("", "end", values=(num_pages, num_words, num_filtered_words, avg_words_per_page, unique_words))
    global stored_words
    stored_words = filtered_words
    loading_label.config(text="File loaded successfully!")



def on_generate_wordcloud():
    if stored_words:
        generate_wordcloud(stored_words)


load_button = tk.Button(root, text="Load PDF", command=load_pdf)
load_button.pack()

loading_label = tk.Label(root, text="")
loading_label.pack()

generate_button = tk.Button(root, text="Generate WordCloud", command=on_generate_wordcloud)
generate_button.pack()


if __name__ == "__main__":
    root.mainloop()
