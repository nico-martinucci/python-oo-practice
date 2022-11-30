from random import randint

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Constructor for new word finder based on file at path"""
        self.path = path
        file = open(self.path)
        self.words = self.parse(file)
        self.report_list_length()

    def __repr__(self):
        return f"<WordFinder path={self.path} num_of_words={len(self.words)}>"

    def random(self):
        """returns random word from instance's words property"""
        randomNum = randint(0, len(self.words)-1)
        return self.words[randomNum]

    def report_list_length(self):
        """prints number of words read"""
        print(f"{len(self.words)} words read")

    def parse(self, file):
        """Reads file and collects lines into list"""
        return file.read().splitlines()


class SpecialWordFinder(WordFinder):
    """SPECIAL Word Finder!"""

    def parse(self, file):
        """Reads file and collects lines into list. Scrubs out all empty lines and lines starting with '#'"""

        return [
            word for word in super().parse(file)
            if word and (not word.startswith("#"))
        ]