from random import choice

#TODO: encapsulate method inside of class
#TODO: use comprehension to make word list
#TODO: add __repr__


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path_to_file):
        """Creates a word list from a file and prints the length of the list"""

        my_file = open(path_to_file, "r")

        self.word_list = self.read_words_to_list(my_file)

        print(f"{len(self.word_list)} words read")

    def read_words_to_list(self, file):
        """takes in and reads a file and turns it into a list of strings"""

        return [word.strip() for word in file]

    def random(self):
        """chooses a random word from the list"""

        random_word = choice(self.word_list)

        return random_word

    def __repr__(self):
        return f"<WordFinder path_to_file={self.path_to_file}"


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary
    but filters out blank lines and lines that start with #"""

    def read_words_to_list(self, file):
        """takes in and reads a file and turns it into a list of strings, accounting
        for lines that start with "#" and empty lines."""

        # return [word.strip() for word in file if not (word.startswith("#") or len(word.strip()) == 0)]
        return [word for word in super().read_words_to_list(file) if not (word.startswith("#") or len(word) == 0)]

    def __repr__(self):
        return f"<Special WordFinder path_to_file={self.path_to_file}"



wf = SpecialWordFinder("complex.txt")
print(wf.word_list)
print(wf.random())
