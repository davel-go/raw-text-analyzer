import re
import spacy
from src.util.data import get_cat_copy

nlp = spacy.load("es_core_news_sm")


class Sentence:
    def __init__(self, text : str):
        self.word_categories_len = None
        self.word_categories = None
        self.content = text
        self.words = re.findall(r'\b[\wáéíóúüñÁÉÍÓÚÜÑ]+\b', text)
        self.syllables = re.findall(r'[aeiouáéíóúü]', text.lower())
        self.avg_word_len, self.word_len_list = self.get_avg_word_len()

    def get_avg_word_len(self):
        word_counts = [len(w) for w in self.words]
        avg_words = sum(word_counts) / len(word_counts) if word_counts else 0
        return avg_words, word_counts

    def pause_positions(self):
        parts = re.split(r'[,:;.\?!]', self.content)
        pauses = [len(p.strip().split()) for p in parts if p.strip()]
        return pauses

    def nlp_analysis(self):
        doc = nlp(self.content)
        categories = get_cat_copy()
        punct_count = 0
        for i, token in enumerate(doc):
            if token.pos_ == "PUNCT":
                punct_count += 1
            info_palabra = {
                "word": token.text,
                "position": i - punct_count + 1,
                "morphology": token.morph.to_dict()
            }

            if token.pos_ in categories:
                categories[token.pos_].append(info_palabra)
            else:
                categories["OTHER"].append(info_palabra)

        self.word_categories = categories
        self.count_word_types()
        return categories

    def count_word_types(self):
        cats = dict()
        for cat, words in self.word_categories.items():
            cats[cat] = len(words)
        self.word_categories_len = cats
        return True

    def __str__(self):
        return self.content

    def pr(self):
        str = f'''
        Sentence provided: {self.content}
        Words in this sentence: {self.words}
        Word count: {len(self.words)}
        Syllables count: {len(self.syllables)}
        AVG word length: {self.avg_word_len}
        Word lengths list: {self.word_len_list}
        '''
        print(str)
