# 🔹 Named Entity Recognition (NER) in NLP

## 🔹 What is NER?

👉 Named Entity Recognition (NER) is the process of identifying and classifying important entities in text.

### 👉 Example:
"Elon Musk is the CEO of Tesla in the USA"

### 👉 Output:
- Elon Musk → PERSON  
- Tesla → ORGANIZATION  
- USA → LOCATION  

---

## 🔹 Setup (Run once)

```python
import nltk
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
```

---

## 🔹 1. Basic NER Example

```python
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

text = "Barack Obama was born in Hawaii"

words = word_tokenize(text)
tags = pos_tag(words)

ner = ne_chunk(tags)

print(ner)
```

---

## 🔹 2. Visual NER Tree

```python
ner.draw()
```

👉 Opens a tree diagram showing entities (PERSON, GPE, etc.)

---

## 🔹 3. Extract Named Entities

```python
entities = []

for chunk in ner:
    if hasattr(chunk, 'label'):
        entity = " ".join(c[0] for c in chunk)
        entity_type = chunk.label()
        entities.append((entity, entity_type))

print(entities)
```

---

## 🔹 4. Multiple Entities Example

```python
text = "Google was founded by Larry Page and Sergey Brin in California"

words = word_tokenize(text)
tags = pos_tag(words)
ner = ne_chunk(tags)

print(ner)
```

---

## 🔹 5. Extract PERSON Entities

```python
persons = []

for chunk in ner:
    if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
        persons.append(" ".join(c[0] for c in chunk))

print(persons)
```

---

## 🔹 6. Extract ORGANIZATION

```python
orgs = []

for chunk in ner:
    if hasattr(chunk, 'label') and chunk.label() == 'ORGANIZATION':
        orgs.append(" ".join(c[0] for c in chunk))

print(orgs)
```

---

## 🔹 7. Extract LOCATION (GPE)

```python
locations = []

for chunk in ner:
    if hasattr(chunk, 'label') and chunk.label() == 'GPE':
        locations.append(" ".join(c[0] for c in chunk))

print(locations)
```

---

## 🔹 8. Loop Output

```python
for chunk in ner:
    if hasattr(chunk, 'label'):
        print(chunk.label(), ":", " ".join(c[0] for c in chunk))
```

---

## 🔹 9. Real-Life Example

```python
text = "Apple is investing $1 billion in India"

words = word_tokenize(text)
tags = pos_tag(words)
ner = ne_chunk(tags)

print(ner)
```

---

## 🔹 10. Full Pipeline

```python
def extract_entities(text):
    words = word_tokenize(text)
    tags = pos_tag(words)
    tree = ne_chunk(tags)

    entities = []

    for chunk in tree:
        if hasattr(chunk, 'label'):
            entity = " ".join(c[0] for c in chunk)
            entities.append((entity, chunk.label()))

    return entities


text = "Elon Musk founded SpaceX in the USA"

print(extract_entities(text))
```

---

## 🔹 Common NER Tags

| Tag | Meaning |
|-----|--------|
| PERSON | Person |
| ORGANIZATION | Company |
| GPE | Country/City |
| LOCATION | Place |
| DATE | Date |
| TIME | Time |
| MONEY | Money |

---

## 🔹 Advantages

✔ Extracts important information  
✔ Useful in chatbots and automation  
✔ Helps in search engines  

---

## 🔹 Disadvantages

❌ Not always accurate  
❌ Context-dependent  

---

## 🔹 Interview Questions

- What is NER?  
- Difference between POS and NER?  
- Use cases of NER?  
- What is GPE?  

---

## 🔹 Interview Answer

👉 NER identifies and classifies entities like names, organizations, and locations in text.

---

## 🚀 Pro Tip

👉 Industry tools:
- SpaCy  
- HuggingFace  
