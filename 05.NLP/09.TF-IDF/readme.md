# 📘 TF-IDF (Term Frequency - Inverse Document Frequency)

## 🚀 Overview
TF-IDF is a numerical statistic used in Natural Language Processing (NLP) to evaluate how important a word is to a document relative to a corpus.

---

## 🧠 Intuition
- Words frequent in a document → Important
- Words frequent across many documents → Less important

---

## ⚙️ Core Components

### 1. Term Frequency (TF)
Measures how often a term appears in a document.

**Formula:**
TF(t, d) = count(t in d) / total terms in d

#### Variants:
- Raw Count
- Normalized TF
- Log Normalization → log(1 + count)
- Binary TF (0 or 1)

---

### 2. Inverse Document Frequency (IDF)
Measures how unique a term is across documents.

**Formula:**
IDF(t) = log(N / df(t))

Where:
- N = total number of documents
- df(t) = number of documents containing term t

#### Variants:
- Standard IDF
- Smoothed IDF → log((1 + N)/(1 + df)) + 1
- Probabilistic IDF → log((N - df)/df)

---

### 3. TF-IDF Formula
TF-IDF(t, d) = TF(t, d) × IDF(t)

---

## 📊 Example

Documents:
- D1: "I love NLP"
- D2: "I love AI"

Vocabulary:
[I, love, NLP, AI]

TF-IDF Result:
- Common words → low score
- Unique words → high score

---

## 🔥 Features of TF-IDF

- Converts text into numerical vectors
- Reduces importance of common words
- Highlights meaningful terms
- Works well with classical ML models
- Fast and computationally efficient

---

## 🧩 Functions & Parameters (Important for Engineers)

### TfidfVectorizer Parameters

- `max_features` → Limits vocabulary size
- `ngram_range` → (1,1), (1,2), etc.
- `stop_words` → Remove common words
- `min_df` → Ignore rare words
- `max_df` → Ignore overly common words
- `sublinear_tf` → Apply log scaling
- `smooth_idf` → Avoid division by zero
- `norm` → l1 or l2 normalization

---

## 🧪 Implementation Example (Python)

```python
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "I love NLP",
    "I love AI"
]

vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words='english')
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
print(X.toarray())
```

---

## 🏗️ Use Cases

- Search Engines
- Document Similarity
- Spam Detection
- Text Classification
- Recommendation Systems

---

## 📐 Cosine Similarity (Used with TF-IDF)

Similarity = cosine(angle between vectors)

---

## ⚡ Advantages

- Simple and fast
- Interpretable
- Works well as baseline
- Low computational cost

---

## ⚠️ Limitations

- Ignores word order
- No semantic understanding
- Cannot capture context
- Poor performance on complex NLP tasks

---

## 🔄 TF-IDF vs Other Methods

| Method | Description |
|-------|------------|
| BoW | Counts word frequency only |
| TF-IDF | Adds importance weighting |
| Word2Vec | Captures semantic meaning |
| BERT | Context-aware embeddings |

---

## 🚀 Best Practices

- Use stopword removal
- Apply n-grams for better context
- Tune max_features
- Normalize vectors
- Combine with ML models (SVM, Logistic Regression)

---

## 🎯 When to Use TF-IDF

Use when:
- Small to medium datasets
- Need fast inference
- Baseline model required

Avoid when:
- Context understanding is required
- Using deep learning models

---

## 📌 Summary

TF-IDF is a foundational NLP technique for feature extraction. While modern NLP uses embeddings and transformers, TF-IDF remains essential for fast, interpretable, and baseline systems.

---

## 📚 References

- Scikit-learn Documentation
- NLP Research Papers

---

✨ End of README

