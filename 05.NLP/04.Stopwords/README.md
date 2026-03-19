# 🔹 Stopwords in NLP

## 🔹 What are Stopwords?

👉 Stopwords are common words that do not add much meaning to a sentence.

### 👉 Examples:
is, the, and, in, on, at, a  

✔ Usually removed to reduce noise in text

---

## 🔹 Setup (Run once)

```python
import nltk
nltk.download('stopwords')
```

---

## 🔹 1. Basic Stopwords Removal

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is a simple example to demonstrate stopwords removal"

words = word_tokenize(text)

filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]

print(filtered_words)
```

---

## 🔹 2. Using Set for Optimization

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

text = "I am learning NLP and it is very interesting"

words = word_tokenize(text)

filtered = [word for word in words if word.lower() not in stop_words]

print(filtered)
```

---

## 🔹 3. Stopwords Removal with Lowercase

```python
text = "This IS an Example of STOPWORDS removal"

words = word_tokenize(text.lower())

filtered = [word for word in words if word not in stop_words]

print(filtered)
```

---

## 🔹 4. Removing Stopwords + Punctuation

```python
import string
from nltk.tokenize import word_tokenize

text = "Hello! This is an example, with punctuation."

words = word_tokenize(text)

filtered = [word for word in words if word.lower() not in stop_words and word not in string.punctuation]

print(filtered)
```

---

## 🔹 5. Custom Stopwords

```python
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

custom_words = {"hello", "example"}

stop_words.update(custom_words)

text = "Hello this is a custom example for NLP"

words = word_tokenize(text)

filtered = [word for word in words if word.lower() not in stop_words]

print(filtered)
```

---

## 🔹 6. Remove Stopwords from Sentence List

```python
sentences = ["I love NLP", "It is very powerful"]

stop_words = set(stopwords.words('english'))

for sentence in sentences:
    words = word_tokenize(sentence)
    filtered = [word for word in words if word.lower() not in stop_words]
    print(filtered)
```

---

## 🔹 7. Stopwords + Stemming

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

text = "I am learning NLP and it is very interesting"

words = word_tokenize(text)

filtered = [stemmer.stem(word) for word in words if word.lower() not in stop_words]

print(filtered)
```

---

## 🔹 8. Stopwords + Lemmatization

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = word_tokenize(text)

filtered = [lemmatizer.lemmatize(word) for word in words if word.lower() not in stop_words]

print(filtered)
```

---

## 🔹 9. Real-Life Example (Search Engine)

```python
query = "What is the best way to learn NLP"

words = word_tokenize(query)

filtered = [word for word in words if word.lower() not in stop_words]

print(filtered)
```

👉 Output:
['best', 'way', 'learn', 'NLP']

---

## 🔹 10. Count Stopwords

```python
words = word_tokenize(text)

count = sum(1 for word in words if word.lower() in stop_words)

print("Stopwords count:", count)
```

---

## 🔹 When NOT to Remove Stopwords

👉 Do NOT remove when:
- Sentiment Analysis  

Example:  
"I am NOT happy"  

❌ Removing "not" changes meaning

---

## 🔹 Advantages

✔ Reduces text size  
✔ Improves model performance  
✔ Removes noise  

---

## 🔹 Disadvantages

❌ May remove important context  
❌ Not suitable for all tasks  

---

## 🔹 Interview Questions

- What are stopwords?  
- Why remove stopwords?  
- When not to remove stopwords?  
- How to customize stopwords?  

---

## 🔹 Interview Answer

👉 “Stopwords are common words like ‘is’, ‘the’, and ‘and’ that are often removed in NLP preprocessing to reduce noise and improve model efficiency.”

---

## 🚀 Pro Tip

👉 Best pipeline:
Tokenization → Stopwords Removal → Lemmatization → Vectorization
