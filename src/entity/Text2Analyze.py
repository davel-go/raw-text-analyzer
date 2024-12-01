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

    def __str__(self):
        txt = ""
        for p in self.paragraphs:
            txt += f"{p}\n"
        return txt
