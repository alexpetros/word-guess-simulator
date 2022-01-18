import sys
import logging

class WordGuess:
    """A single play of the word-guessing game.

    WordGuess represents a single run of the guessing game. A game consists of
    successive guesses until either the word is guessed or the player runs out
    of turns.

    An instance of WordGuess contains all the relevant information about the
    game as instance variables, most importantly:
        - self.turn (starts at 0, increments after a call to self.guess_word)
        - self.victory (True if the player guessed the correct word, else False)
        - self.word (the winning word)

    Games cannot be restarted once complete; initialize a new instance if a new
    game is desired.
    """
    DICTIONARY_FILE = './words'
    MAX_GUESSES = 6

    # Character representations of the hint types
    CORRECT = '*'
    MISPLACED = '?'
    NOT_PRESENT = 'x'

    def __init__(self, word, word_dict=None):
        """Initialize a new word game."""
        self.turn = 0
        self.victory = False
        self.word = word
        self.word_dict = word_dict

        if word_dict is None:
            f = open(WordGuess.DICTIONARY_FILE, 'r')
            self.word_dict = { word.rstrip() for word in f.readlines() }
            f.close()

        logging.debug('word is: ' + self.word)

    def has_guess_left(self):
        """Return True if the player can still guess again."""
        return not self.victory and self.turn < WordGuess.MAX_GUESSES

    def guess_word(self, guess):
        """
        Guess a word, increment self.turns, and return a hint from the guess.

        Each guess returns a hint in the form of a formatted string. Each
        character in the string will be one of three characters

            - WordGuess.CORRECT ('*')
            - WordGuess.MISPLACED ('?')
            - WordGuess.NOT_PRESENT ('x')

        where the character in parethenthesis is the printed form. For example,
        if the game word is "spear" and the function is called with "spark", it
        will return "**??x"; the first two letters are correct, the second two
        are present in the word but misplaced, and the final one is not present
        at all.

        Note that if the word only includes one instance of a character but the
        guess includes two, the second letter will be marked as if it were an
        entirely different character i.e. if the letter "a" appears once in a
        word, the second "a" in the guess will be marked at NOT_PRESENT.

        While the hint characters are unlikely to change, it is best to refer to
        the hint characters using their class constants instead of their
        character value for readability purposes.
        """
        if not self.has_guess_left():
            raise Exception('Attempted to guess word for game that is over. Aborting.')
        if len(guess) != len(self.word):
            print(f'Error! Guess should be {len(self.word)} characters long, received: {len(guess)}', file=sys.stderr)
            return ""
        if guess not in self.word_dict:
            print(f'Error! Word "{guess}" not found in dictionary.', file=sys.stderr)
            return ""

        # Generate character map
        word_list = list(self.word)
        remaining_letters = { char:word_list.count(char) for char in word_list }

        # Conduct next turn
        hint = ""
        self.turn += 1
        if guess == self.word:
            self.victory = True
            return WordGuess.CORRECT * len(self.word)

        for i in range(len(guess)):
            char = guess[i]
            if char == self.word[i]:
                hint += WordGuess.CORRECT
                remaining_letters[char] -= 1
            elif char in remaining_letters and remaining_letters[char] > 0:
                hint += WordGuess.MISPLACED
                remaining_letters[char] -= 1
            else:
                hint += WordGuess.NOT_PRESENT

        return hint


