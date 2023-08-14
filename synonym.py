from pyvi import ViTokenizer
from pyvi import ViUtils
from nltk.corpus import wordnet

# Tách từ và chuẩn hóa văn bản tiếng Việt
text = "Đây là một câu ví dụ về nhận dạng từ đồng nghĩa"
tokenized_text = ViTokenizer.tokenize(text)
normalized_text = ViUtils.remove_accents(tokenized_text)

# Nhận dạng từ đồng nghĩa của từ "ví dụ"
synonyms = []
word = "Quản trị kinh doanh"
for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(synonyms)