from random import randint

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Constructor for new word finder based on file at path"""
        file = open(path)
        self.words = file.read().splitlines()
        print(f"{len(self.words)} words read")
        # call self.method that prints word length

    def __repr__(self):
        return f"<>"

    def random(self):
        """returns random word from instance's words property"""
        randomNum = randint(0, len(self.words)-1)
        return self.words[randomNum]
    # method that prints word length -- "A"
    def report_list_length(self):
        

class SpecialWordFinder(WordFinder):
    """SPECIAL Word Finder!"""

    def __init__(self, path):
        """Constructor for new SPECIAL word finder, based on file at path"""
        super().__init__(path)
        self.scrub_blanks_and_hashes()
    
    def scrub_blanks_and_hashes(self):
        """Scrubs out all empty lines and lines starting with '#'"""
        self.words = [
            word for word in self.words 
            if word and (not word[0] == "#")
        ]

    # redefine method "A" here