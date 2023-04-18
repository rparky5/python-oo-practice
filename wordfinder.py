from random import choice

#TODO: encapsulate method inside of class
#TODO: use comprehension to make word list
#TODO: add __repr__


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path_to_file):
        """Creates a word list from a file and prints the length of the list"""

        self.word_list = self.read_words_to_list(path_to_file)

        print(f"{len(self.word_list)} words read")

    def read_words_to_list(self, file):
        """takes in and reads a file and turns it into a list of strings"""

        my_file = open(file, "r")

        return [word.strip() for word in my_file]

    def random(self):
        """chooses a random word from the list"""

        random_word = choice(self.word_list)
        
        return random_word


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary
    but filters out blank lines and lines that start with #"""
    # def __init__(self, path_to_file):
    #     """Creates a filtered word list from a file and prints the length of the list"""
    #     super().__init__(path_to_file)
    #     self.word_list = [word for word in self.word_list if not (word.startswith("#") or word == "")]



# wf = SpecialWordFinder("gistfile1.txt")
# print(wf.word_list)
# print(wf.random())
