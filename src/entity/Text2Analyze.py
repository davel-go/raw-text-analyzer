from src.entity.Paragraph import Paragraph
from collections import Counter
import re


class Text2Analyze:
    def __init__(self, text):
        self.pp = None
        paragraphs = re.split(r'\n+', text)
        self.content = text
        self.paragraphs: [Paragraph] = [Paragraph(p.strip()) for p in paragraphs if p.strip()]
        self.senteces_per_paragraph = [len(p.sentences) for p in self.paragraphs]

    def pause_positions(self):
        if self.pp is None:
            self.pp = [item for p in self.paragraphs for item in p.pause_positions]
        return self.pp

    def word_count_list(self):
        return [words for p in self.paragraphs for words in p.word_count]

    def word_freq(self):
        palabras = re.findall(r'\b[\wáéíóúüñÁÉÍÓÚÜÑ]+\b', self.content.lower())
        freq = Counter(palabras)
        return dict(freq)

    def char_count(self):
        return sum([sum(p.char_count) for p in self.paragraphs])

    def word_len_list(self):
        ls = list()
        for p in self.paragraphs: ls += p.word_len_list
        return ls

    def sentence_count(self):
        return sum(self.senteces_per_paragraph)

    def avg_word_len(self):
        return round(sum([p.avg_word_len for p in self.paragraphs]) / len(self.paragraphs), 2)

    def avg_senteces_per_paragraph(self):
        return round(self.sentence_count() / len(self.paragraphs), 2)

    def __str__(self):
        txt = ""
        for p in self.paragraphs:
            txt += f"{p}\n"
        return txt

    def show_stats(self):
        char_count = self.char_count()
        word_count = self.word_count_list()

        txt = f'''
        ============================================================
        Paragraph count:    {len(self.paragraphs)}
                Sentences in each paragraph:            {self.senteces_per_paragraph}
                Average of sentences in each paragraph: {self.avg_senteces_per_paragraph()}
        Sentence count:     {self.sentence_count()}
        Character count:    {char_count}
        Word count:         {sum(word_count)}
                Word count list (words per sentence):   {word_count}
                Word lengths list (length of words):    {self.word_len_list()}
                Avg word length:                        {self.avg_word_len()}        
        ============================================================
        Pause positions: {self.pause_positions()}
                Avg pause:                              {round( sum(self.pause_positions()) / len(self.pause_positions()), 2)}
        '''
        print(txt)
