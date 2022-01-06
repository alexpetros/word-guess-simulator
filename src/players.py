import string
import random
import logging
from game import WordGuess

class HumanPlayer():
    def get_guess(self, game, previous_clue):
        print(previous_clue[1])
        return input(
            f'{game.MAX_GUESSES - game.turn} guesses left. Enter a guess:\n')

class HardModeBasic():
    def __init__(self, words_list):
        word_length = len(words_list[0])

        self.words_list = words_list
        self.known_chars = [""] * word_length
        self.invalid_placements = [""] * word_length
        self.max_chars = { c: word_length for c in string.ascii_lowercase } 
        logging.debug('Starting new game')

    def get_guess(self, game, previous_clue):
        logging.debug('Hint is: ' + previous_clue[1])

        misplaced_chars = ""
        for i, char in enumerate(previous_clue[0]):
            if previous_clue[1][i] == WordGuess.CORRECT:
                self.known_chars[i] = char
            elif previous_clue[1][i] == WordGuess.MISPLACED:
                misplaced_chars += char
                if char not in self.invalid_placements[i]:
                    self.invalid_placements[i] += char

        for i, char in enumerate(previous_clue[0]):
            if previous_clue[1][i] == WordGuess.NOT_PRESENT:
                self.max_chars[char] = (misplaced_chars.count(char) +
                                        self.known_chars.count(char))
        
        # Filter out all the words that no longer apply
        self.words_list = list(filter(self.is_valid, self.words_list))
        logging.debug(f'Known characters: {self.known_chars}')
        logging.debug(f'Invalid placements {self.invalid_placements}')
        logging.debug(f'Max characters: {self.max_chars}')

        guess = random.choice(self.words_list)
        logging.debug('Guess is: ' + guess)
        return guess

    def is_valid(self, word):
        for i, char in enumerate(word):
            if self.known_chars[i] != "" and self.known_chars[i] != char:
                return False
            if char in self.invalid_placements[i]:
                return False

        for char in self.max_chars.keys():
            if word.count(char) > self.max_chars[char]:
                return False

        return True
