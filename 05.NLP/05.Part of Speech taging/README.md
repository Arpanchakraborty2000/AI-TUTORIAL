# 🔹 Parts of Speech (POS) Tagging in NLP

## 🔹 What is POS Tagging?

👉 POS Tagging means assigning a grammatical label to each word.

### 👉 Examples:
- Noun (NN) → boy, car  
- Verb (VB) → run, eat  
- Adjective (JJ) → happy, fast  
- Adverb (RB) → quickly  

---

## 🔹 Setup (Run once)

```python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```

---

## 🔹 1. Basic POS Tagging

```python
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "I love learning NLP"

words = word_tokenize(text)
tagged = pos_tag(words)

print(tagged)
```

---

## 🔹 2. Extract Nouns, Verbs, Adjectives, Adverbs

```python
words = word_tokenize("The boy is playing with a ball")
tagged = pos_tag(words)

nouns = [w for w, t in tagged if t.startswith('NN')]
verbs = [w for w, t in tagged if t.startswith('VB')]
adjectives = [w for w, t in tagged if t.startswith('JJ')]
adverbs = [w for w, t in tagged if t.startswith('RB')]

print("Nouns:", nouns)
print("Verbs:", verbs)
print("Adjectives:", adjectives)
print("Adverbs:", adverbs)
```

---

## 🔹 3. POS Tagging + Lemmatization

```python
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def get_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN

words = word_tokenize("The boys are running faster")
tagged = pos_tag(words)

lemmatized = [lemmatizer.lemmatize(w, get_pos(t)) for w, t in tagged]

print(lemmatized)
```

---

## 🔹 Real-Life Example

```python
text = "Book a flight to Delhi tomorrow"

words = word_tokenize(text)
tagged = pos_tag(words)

print(tagged)
```

---

## 🔹 Common POS Tags

| Tag | Meaning |
|-----|--------|
| NN | Noun |
| NNP | Proper Noun |
| VB | Verb |
| VBG | Verb (ing) |
| JJ | Adjective |
| RB | Adverb |

---

## 🔹 Interview Answer

👉 POS tagging assigns grammatical labels to words and helps understand sentence structure.

---

## 🚀 Pipeline

Text → Tokenization → Stopwords → POS Tagging → Lemmatization → Vectorization
