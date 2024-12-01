import re


class Sentence:
    def __init__(self, text : str):
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
