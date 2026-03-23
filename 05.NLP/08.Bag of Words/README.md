# 📘 Bag of Words (BoW) in NLP

## What is Bag of Words (BoW)?
Bag of Words (BoW) is a technique in Natural Language Processing (NLP) used to convert text into numerical vectors.

**It treats text as a bag of words, ignoring:**
- grammar
- word order

**It only considers:**
- which words appear
- how many times they appear

---

## 🧠 Example (Basic BoW)

**Sentences:**
- S1: "I love NLP"
- S2: "I love coding"

**Step 1: Vocabulary**
```
[I, love, NLP, coding]
```

**Step 2: Vector Representation**

| Sentence | I | love | NLP | coding |
|----------|--|------|-----|--------|
| S1       | 1 | 1    | 1   | 0      |
| S2       | 1 | 1    | 0   | 1      |

---

## 🔄 Types of Bag of Words (with Examples)

### 1️⃣ Binary Bag of Words (Presence/Absence)
Only checks whether a word exists (1) or not (0)

**Example:**
Sentence: "NLP NLP is fun"

Vocabulary:
```
[NLP, is, fun]
```

Vector:
```
[1, 1, 1]
```

---

### 2️⃣ Count-Based Bag of Words (Frequency)
Counts how many times each word appears

**Example:**
Sentence: "NLP NLP is fun"

Vector:
```
[2, 1, 1]
```

---

### 3️⃣ N-gram Bag of Words
Considers sequences of words

**Example:**
Sentence: "I love NLP"

- Unigram: [I, love, NLP]
- Bigram: [I love, love NLP]
- Trigram: [I love NLP]

---

### 4️⃣ Term Frequency (TF)
Measures importance of a word in a document

```
TF = (Number of times word appears) / (Total words in document)
```

**Example:**
Sentence: "NLP is fun and NLP is easy"

- Total words = 7
- NLP appears = 2

```
TF(NLP) = 2 / 7 = 0.28
```

---

### 5️⃣ TF-IDF (Term Frequency – Inverse Document Frequency)
Improves BoW by reducing importance of common words

```
TF-IDF = TF × IDF
```

```
IDF = log(Total Documents / Documents containing word)
```

---

### 6️⃣ Hashing Vectorizer
Uses a hash function instead of storing vocabulary

---

### 7️⃣ One-Hot Encoding
Each word is represented as a vector

```
I     → [1, 0, 0]
love  → [0, 1, 0]
NLP   → [0, 0, 1]
```

---

## ⚡ Combined Example

Sentence: "I love NLP NLP"

| Type   | Representation |
|--------|---------------|
| Binary | [1, 1, 1]     |
| Count  | [1, 1, 2]     |
| TF     | [1/4, 1/4, 2/4] |

---

## ⚖️ Advantages vs Disadvantages

| Aspect | Advantages ✅ | Disadvantages ❌ |
|--------|-------------|----------------|
| Simplicity | Easy to implement | Too simple |
| Speed | Fast | Slow for large vocab |
| Interpretability | Easy to understand | No context |
| Feature Size | Numeric conversion | High dimensional |
| Word Order | Not required | Ignored |
| Context | Works basic tasks | No semantics |
| Memory | Good small data | Heavy large data |

---

## 🧾 Summary

| Type | Key Idea |
|------|---------|
| Binary | Presence |
| Count | Frequency |
| N-gram | Sequence |
| TF | Importance |
| TF-IDF | Weighted |
| Hashing | Efficient |
| One-hot | Word vector |

---

## 🎯 Interview Summary
BoW is simple, fast, and interpretable but fails to capture context, word order, and semantics.
