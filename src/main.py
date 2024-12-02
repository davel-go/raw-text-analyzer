from src.entity.Text2Analyze import Text2Analyze
from src.util.data import read_file

text = read_file()
txt = Text2Analyze(text)
print("Word count list: ", txt.word_count_list())
print("Pause positions: ", txt.pause_positions())