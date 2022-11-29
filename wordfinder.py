from random import randint

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        # learn how to get file path
        file = open(path)
        self.words = file.read().splitlines()

        print(self.words)

    def random(self):
        #from self.words, invoke randInt
        randomNum = randint(0, len(self.words)-1)
        return self.words[randomNum]