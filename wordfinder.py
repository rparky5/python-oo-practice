from random import choice

def read_words_to_list(file):
    my_file = open(file, "r")
    words = my_file.read()
    word_list = words.split("\n")
    return word_list

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path_to_file):
        self.word_list = read_words_to_list(path_to_file)
        print(f"{len(self.word_list)} words read")

    def random(self):
        random_word = choice(self.word_list)
        return random_word

wf = WordFinder("gistfile1.txt")
print(wf.random())