import spacy

from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_lg")
matcher = Matcher(nlp.vocab)
# Add ID "DailyDialog"
pattern = [{"POS": "PRON"}, {"POS": "VERB"}, {'OP': '*'}, {"POS": "NOUN"}]
matcher.add("DailyDialog", None, pattern)

#text = 'i like this and that and also banans'
with open('dialogues_text.txt') as f:
    text = f.read()
doc = nlp(text)

matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]  # span
    print(match_id, string_id, start, end, span.text)

def most_similar(word):
    by_similarity = sorted(word.vocab, key=lambda w: word.similarity(w), reverse=True)
    return [w.orth_ for w in by_similarity[:10]]

def most_similar_rar(word):
    queries = [w for w in word.vocab if w.is_lower == word.is_lower and w.prob >= -15]
    by_similarity = sorted(queries, key=lambda w: word.similarity(w), reverse=True)
    return by_similarity[:20]

