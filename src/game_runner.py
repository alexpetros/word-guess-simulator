import random
from game import WordGuess

def play_game(game, player, initial=None, show_games=True):
    """
    Play the game and return num_guesses if it was won, -1 if it was lost.

    The two positional arguments are an instance of WordGuess and a Player
    object. The only requirement for the player is that it implement
    self.get_guess(game, previous_clue), where previous_clue is a (str, str)
    tuple that contains the previous guess and previous hint, respectively.

    If you would like to make use of any additional data for the Player (like a
    full history of guesses), that is the responsibility of the Player to store.
    """
    guesses = []
    previous_clue = ("", "")
    while game.has_guess_left():
        if len(guesses) == 0 and initial is not None:
            guess = initial
        else:
            guess = player.get_guess(game, previous_clue)
        hint = game.guess_word(guess)
        if hint != "":
            guesses.append(guess)
            previous_clue = (guess, hint)

    result = game.turn if game.victory else -1
    if show_games:
        print(f'{game.word},{result},' + ','.join(g for g in guesses))
    return result

class GameRunner:
    def __init__(self, word_list, word_size=5, show_games=True):
        """
        Initialize the game with a list of words.

        Keyword arguments:
        word_size -- the length of the word to be guessed
        show_games -- if True, outputs the result of each individual game

        If you elect to output the games, each game is printed to STDOUT in the
        following comma-separated format:
        CORRECT_WORD, NUM_GUESSES, [PLAYER GUESSES...]

        A game with the winning word "spear", where the player guessed it on the
        third try, would be output as:
        spear,3,track,spike,spear

        The second value will be -1 if the game was lost.
        """
        self.show_games = show_games
        self.word_list = list(filter(
            lambda w: (len(w) == word_size and w[0].islower()), word_list))

        # The list is for quick random selection; the set for quick lookup
        self.word_dict = set(self.word_list)

    def play_games(self, num_games, playerObj, initial=None):
        """Play num games, return: (win rate, average num of guesses to win)."""
        num_wins = 0
        total_turns = 0
        for i in range(num_games):
            game = WordGuess(random.choice(self.word_list), self.word_dict)
            result = play_game(game, playerObj(self.word_list), initial=initial,
                               show_games=self.show_games)
            if result != -1:
                num_wins += 1
                total_turns += result

        return num_wins / num_games, total_turns / num_games

