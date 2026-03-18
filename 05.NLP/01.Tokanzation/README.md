# 🔹 Tokenization in NLP

## 🔹 What is Tokenization in NLP?

Tokenization is the process of breaking down a piece of text into smaller units called **tokens**.

These tokens can be:
- Words
- Sentences
- Subwords
- Characters

👉 **Example:**

Sentence:  
"I love AI and Machine Learning"  

Tokens:  
["I", "love", "AI", "and", "Machine", "Learning"]

---

## 🔹 Types of Tokenization

### 1. Word Tokenization
Splits text into words  

👉 Example:  
"ChatGPT is powerful" → ["ChatGPT", "is", "powerful"]

---

### 2. Sentence Tokenization
Splits text into sentences  

👉 Example:  
"I love AI. It is amazing." →  
["I love AI.", "It is amazing."]

---

### 3. Character Tokenization
Breaks text into characters  

👉 Example:  
"AI" → ["A", "I"]

---

### 4. Subword Tokenization (Advanced)
Used in modern AI models (like GPT, BERT)  

👉 Example:  
"unhappiness" → ["un", "happi", "ness"]  

✔ Helps handle unknown words efficiently

---

## 🔹 Why Tokenization is Important?

- Converts text into a format machines can understand  
- First step in any NLP pipeline  
- Helps in:
  - Text classification  
  - Sentiment analysis  
  - Machine translation  
  - Chatbots  

---

## 🔹 Simple Interview Answer (Short Version)

👉 "Tokenization is the process of breaking text into smaller units like words, sentences, or subwords. It is the first step in NLP and helps machines understand and process text data. It is used in applications like chatbots, search engines, and sentiment analysis."

---

# 🔹 NLTK Tokenization Examples

---

## 🔹 1. Sentence Tokenization

```python
import nltk
nltk.download('punkt')  # run once

from nltk.tokenize import sent_tokenize

text = """The quick brown fox jumps over the lazy dog.
NLP is very interesting. Let's learn it step by step."""

sentences = sent_tokenize(text)

print(sentences)
```

---

## 🔹 2. Word Tokenization

```python
from nltk.tokenize import word_tokenize

text = "I love learning NLP with Python!"

words = word_tokenize(text)

print(words)
```

---

## 🔹 3. Character Tokenization

```python
text = "NLP"

chars = list(text)

print(chars)
```

---

## 🔹 4. WordPunct Tokenization

```python
from nltk.tokenize import WordPunctTokenizer

text = "Hello!!! How are you??"

tokenizer = WordPunctTokenizer()
tokens = tokenizer.tokenize(text)

print(tokens)
```

---

## 🔹 5. Regexp Tokenization (Custom Rules)

```python
from nltk.tokenize import RegexpTokenizer

text = "My phone number is 9876543210 and email is test@gmail.com"

tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)

print(tokens)
```

---

## 🔹 6. Tweet Tokenization (Social Media)

```python
from nltk.tokenize import TweetTokenizer

text = "I love NLP 😊🔥 #AI #MachineLearning"

tokenizer = TweetTokenizer()
tokens = tokenizer.tokenize(text)

print(tokens)
```

---

## 🔹 7. N-grams (Advanced Tokenization)

```python
from nltk.util import ngrams

text = "I love NLP"
tokens = text.split()

bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
```

---

## 🔹 Real-Life Example (Chatbot)

```python
from nltk.tokenize import word_tokenize

user_input = "Book a flight to Delhi tomorrow"

tokens = word_tokenize(user_input)

print(tokens)
```

---

## 🔹 Quick Summary (Interview Ready)

👉 “Tokenization is the process of breaking text into smaller units such as sentences, words, or subwords. In NLTK, we perform sentence tokenization using `sent_tokenize()` and word tokenization using `word_tokenize()`. It is the first step in NLP pipelines and is used in chatbots, search engines, and sentiment analysis.”
