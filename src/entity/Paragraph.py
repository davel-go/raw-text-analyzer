from src.entity.Sentence import Sentence
from src.util.data import get_cat_copy, get_cat_num_copy
import re


class Paragraph:
    def __init__(self, text):
        self.avg_word_categories_len = None
        self.word_categories_len = None
        self.word_categories = None
        self.content = text
        self.sentences: [Sentence] = [Sentence(s.strip()) for s in re.split(r'[.!?]', text) if s.strip()]
        for s in self.sentences:
            s.nlp_analysis()
        self.char_count = [len(s.content) for s in self.sentences]
        self.word_count = [len(s.words) for s in self.sentences]
        self.word_len_list = [item for s in self.sentences for item in s.word_len_list]
        self.avg_word_len = sum(self.word_len_list) / len(self.word_len_list)
        self.pause_positions = [item for s in self.sentences for item in s.pause_positions()]
        self.combine_word_categories()
        self.combine_word_categories_len()
        self.calculate_avg_word_categories()

    def combine_word_categories(self):
        self.word_categories = get_cat_copy()
        for s in self.sentences:
            for category, words in s.word_categories.items():
                self.word_categories[category].extend(words)

    def combine_word_categories_len(self):
        categories = get_cat_num_copy()
        for c, words in categories.items():
            categories[c] = sum(s.word_categories_len.get(c) for s in self.sentences)
        self.word_categories_len = categories
    
    def calculate_avg_word_categories(self):
        categories = get_cat_num_copy()
        for c, words in categories.items():
            categories[c] = round(sum(s.word_categories_len.get(c) for s in self.sentences) / len(self.sentences), 2)
        self.avg_word_categories_len = categories

    def __str__(self):
        txt = ""
        for s in self.sentences:
            txt += f"{s}\n"
        return txt
