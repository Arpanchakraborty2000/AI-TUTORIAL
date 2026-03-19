# 🔹 One-Hot Encoding in NLP

## 🔹 What is One-Hot Encoding?

👉 One-Hot Encoding is a technique used to convert text (words) into a numerical format so that machines can understand it.

👉 Each word is represented as a vector of 0s and 1s:
- Only one position is 1
- All others are 0

---

## 🔹 Simple Example

Sentence:
I love NLP

Vocabulary:
["I", "love", "NLP"]

### 👉 One-Hot Representation:

| Word | Vector |
|------|--------|
| I    | [1, 0, 0] |
| love | [0, 1, 0] |
| NLP  | [0, 0, 1] |

---

## 🔹 How it Works

1. Create a vocabulary (unique words)
2. Assign an index to each word
3. Create a vector of size = vocabulary length
4. Put 1 at index of word, rest = 0

---

## 🔹 Python Example

```python
from sklearn.preprocessing import OneHotEncoder
import numpy as np

words = np.array(["I", "love", "NLP"]).reshape(-1, 1)

encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(words)

print(encoded)
```

---

## 🔹 Manual Example

```python
words = ["I", "love", "NLP"]

vocab = list(set(words))

one_hot = {}

for i, word in enumerate(vocab):
    vector = [0] * len(vocab)
    vector[i] = 1
    one_hot[word] = vector

print(one_hot)
```

---

## 🔹 Real-Life Use

👉 Used in:
- Text Classification  
- Spam Detection  
- Chatbots  

Example:
"spam" → [1, 0]  
"not spam" → [0, 1]

---

## 🔹 Advantages

✔ Simple to understand  
✔ Easy to implement  
✔ Works well for small datasets  

---

## 🔹 Disadvantages

❌ High memory usage  
❌ No semantic meaning  
❌ Sparse vectors  

---

## 🔹 One-Hot vs Embeddings

| Feature | One-Hot | Embeddings |
|--------|--------|-----------|
| Meaning | No | Yes |
| Size | Large | Small |
| Relation | None | Captures similarity |

---

## 🔹 Interview Questions

- What is One-Hot Encoding?  
- Why not use it always?  
- What is its drawback?  

---

## 🔹 Interview Answer

👉 One-hot encoding converts words into binary vectors where only one value is 1 and others are 0.

---

## 🚀 Pro Tip

👉 Use:
- Word2Vec  
- GloVe  
- BERT  

instead of one-hot encoding in real-world NLP.
