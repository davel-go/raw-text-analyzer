from src.entity.Paragraph import Paragraph
from collections import Counter
import re


class Text2Analyze:
    def __init__(self, text):
        paragraphs = re.split(r'\n+', text)
        self.content = text
        self.paragraphs: [Paragraph] = [Paragraph(p.strip()) for p in paragraphs if p.strip()]

    def pause_positions(self):
        return [item for p in self.paragraphs for item in p.pause_positions]

    def word_count_list(self):
        return [words for p in self.paragraphs for words in p.word_count]

    def word_freq(self):
        palabras = re.findall(r'\b[\wáéíóúüñÁÉÍÓÚÜÑ]+\b', self.content.lower())
        freq = Counter(palabras)
        return dict(freq)

    def char_count(self):
        return sum([sum(p.char_count) for p in self.paragraphs])

    def avg_word_len(self):
        return sum([p.avg_word_len for p in self.paragraphs]) / len(self.paragraphs)

    def word_len_list(self):
        ls = list()
        for p in self.paragraphs: ls += p.word_len_list
        return ls

    def __str__(self):
        txt = ""
        for p in self.paragraphs:
            txt += f"{p}\n"
        return txt

    def show_stats(self):
        char_count = self.char_count()
        word_count = self.word_count_list()
        txt = f'''
        Character count in this text: {char_count}
        Word count in this text: {sum(word_count)}
        Paragraph count: {len(self.paragraphs)}
        =================
        Word count list: {word_count}
        Word lengths list: {self.word_len_list()}
        Avg word length: {self.avg_word_len()}
        =================
        Pause positions: {self.pause_positions()}
        '''
        print(txt)
