# 🔹 Stemming in NLP

## 🔹 What is Stemming?

👉 Stemming is the process of reducing a word to its root/base form.

Example:

running → run  
playing → play  
studies → studi  

⚠️ Output may not always be a real word (rule-based)

---

## 🔹 Types of Stemming in NLTK

### ✅ 1. Porter Stemmer (Most Common)

👉 Oldest and widely used algorithm

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "runs", "ran", "easily", "fairly"]

for word in words:
    print(f"{word} → {stemmer.stem(word)}")
```

✅ Output:
running → run  
runs → run  
ran → ran  
easily → easili  
fairly → fairli  

---

### ✅ 2. Snowball Stemmer (Better Version)

👉 Improved version of Porter, supports multiple languages

```python
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("english")

words = ["running", "runs", "ran", "easily", "fairly"]

for word in words:
    print(f"{word} → {stemmer.stem(word)}")
```

✅ Output:
running → run  
runs → run  
ran → ran  
easily → easili  
fairly → fair  

---

### ✅ 3. Lancaster Stemmer (Aggressive)

👉 Very aggressive — may over-stem words

```python
from nltk.stem import LancasterStemmer

stemmer = LancasterStemmer()

words = ["running", "runs", "ran", "happiness", "studies"]

for word in words:
    print(f"{word} → {stemmer.stem(word)}")
```

✅ Output:
running → run  
runs → run  
ran → ran  
happiness → happy  
studies → study  

---

## 🔥 Comparison Example

```python
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer

porter = PorterStemmer()
snowball = SnowballStemmer("english")
lancaster = LancasterStemmer()

word = "happiness"

print("Porter     →", porter.stem(word))
print("Snowball   →", snowball.stem(word))
print("Lancaster  →", lancaster.stem(word))
```

✅ Output:
Porter     → happi  
Snowball   → happi  
Lancaster  → happy  

---

## 🔹 Real-Life Example (Search Engine)

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

search_words = ["connecting", "connection", "connected"]

for word in search_words:
    print(stemmer.stem(word))
```

👉 Output:
connect  
connect  
connect  

✔ Helps match similar words in search

---

## 🔹 When to Use Which?

| Stemmer   | Use Case |
|----------|---------|
| Porter   | Basic NLP tasks |
| Snowball | Better accuracy (recommended) |
| Lancaster| Fast but aggressive |

---

## 🔹 Stemming vs Lemmatization

| Feature | Stemming | Lemmatization |
|--------|---------|--------------|
| Output | Not always real word | Real word |
| Speed | Fast | Slower |
| Accuracy | Low | High |

---

## 🔹 Interview Answer

👉 “Stemming is a technique used in NLP to reduce words to their root form using rule-based approaches. Common stemmers include Porter, Snowball, and Lancaster. It helps in text normalization for tasks like search engines and text classification.”

---

## 🚀 Pro Tip

👉 In real projects:
- Use SnowballStemmer (better)
- Or prefer Lemmatization (industry standard)
