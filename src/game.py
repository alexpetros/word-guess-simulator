import sys

class WordGuess():
    DICTIONARY_FILE = './words'
    MAX_GUESSES = 6

    # String representations of the hint types
    CORRECT = '*'
    MISPLACED = '?'
    NOT_PRESENT = 'x'

    def __init__(self, word, words_dict = None):
        """Initialize the game with the word provided, and optionally, the dictionary."""
        self.turn = 0
        self.victory = False
        self.word = word
        self.words_dict = words_dict

        if words_dict == None:
            f = open(WordGuess.DICTIONARY_FILE, 'r')
            self.words_dict = { word.rstrip() for word in f.readlines() }

    def has_guess_left(self):
        """Return True if the player can still guess again."""
        return not self.victory and self.turn < WordGuess.MAX_GUESSES

    def guess_word(self, guess):
        """Guess a word and return a string that describes how close the guess was."""

        # Handle error cases
        if not self.has_guess_left():
            raise Exception('Attempted to guess word for game that is over. Aborting.')
        if len(guess) != len(self.word):
            print(f'Error! Guess should be {len(self.word)} characters long, received: {len(guess)}', file=sys.stderr)
            return ""
        if guess not in self.words_dict:
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


# If this file is run directly, start an interactive game in the command line
if __name__ == '__main__':
    game = WordGuess('tiger')
    print('Starting a new game!')

    while game.has_guess_left():
        guess = input(f'{game.MAX_GUESSES - game.turn} guesses left. Enter a guess:\n')
        result = game.guess_word(guess)

        if result != "":
            print(result)

