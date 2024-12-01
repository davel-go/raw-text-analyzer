from src.entity.Sentence import Sentence
import re


class Paragraph:
    def __init__(self, text):
        self.content = text
        self.sentences: [Sentence] = [Sentence(s.strip()) for s in re.split(r'[.!?]', text) if s.strip()]
        self.char_count = [len(s.content) for s in self.sentences]
        self.word_count = [len(s.words) for s in self.sentences]
        self.pause_positions = [item for s in self.sentences for item in s.pause_positions()]

    def __str__(self):
        txt = ""
        for s in self.sentences:
            txt += f"{s}\n"
        return txt
