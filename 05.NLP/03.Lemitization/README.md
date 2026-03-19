# 🔹 Lemmatization in NLP

## 🔹 What is Lemmatization?

👉 Lemmatization is the process of converting a word into its base dictionary form (lemma) using vocabulary and context.

### 👉 Example:
running → run  
better → good  
studies → study  

✔ Produces meaningful words (unlike stemming)

---

## 🔹 Setup (Run once)

```python
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
```

---

## 🔹 1. Basic Lemmatization (Default = Noun)

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["cars", "buses", "children"]

for word in words:
    print(word, "→", lemmatizer.lemmatize(word))
```

---

## 🔹 2. Verb Lemmatization

👉 Important: specify `pos='v'`

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["running", "ran", "eating"]

for word in words:
    print(word, "→", lemmatizer.lemmatize(word, pos='v'))
```

---

## 🔹 3. Adjective Lemmatization

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["better", "best", "faster"]

for word in words:
    print(word, "→", lemmatizer.lemmatize(word, pos='a'))
```

---

## 🔹 4. Adverb Lemmatization

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["quickly", "slowly"]

for word in words:
    print(word, "→", lemmatizer.lemmatize(word, pos='r'))
```

---

## 🔹 5. POS Tagging + Lemmatization (Advanced)

```python
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

text = "The boys are running faster than the girls"

tokens = word_tokenize(text)
tagged = pos_tag(tokens)

lemmatized = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in tagged]

print(lemmatized)
```

---

## 🔹 6. Sentence Lemmatization

```python
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

text = "The children are playing with better toys"

words = word_tokenize(text)

lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]

print(lemmatized_words)
```

---

## 🔹 7. Real-Life Example

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

user_input = ["running", "runs", "ran"]

for word in user_input:
    print(lemmatizer.lemmatize(word, pos='v'))
```

---

## 🔹 Stemming vs Lemmatization

| Feature | Stemming | Lemmatization |
|--------|---------|--------------|
| Output | Not real word | Real word |
| Accuracy | Low | High |
| Speed | Fast | Slower |

---

## 🔹 Interview Answer

👉 “Lemmatization converts words into their base form using context and vocabulary, producing meaningful words.”

---

## 🚀 Pro Tips

👉 Use:
- pos='v' for verbs  
- pos='a' for adjectives  

👉 Pipeline:
Tokenization → Stopwords → Lemmatization → Vectorization
