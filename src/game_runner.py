import logging, random
from game import WordGuess

def play_game(game, player):
    """Play game and return num guesses if win, -1 if loss."""
    previous_clue = ("", "")
    while game.has_guess_left():
        guess = player.get_guess(game, previous_clue)
        hint = game.guess_word(guess)
        if hint != "":
            previous_clue = (guess, hint)

    result = game.turn if game.victory else -1
    logging.info(f'Game result: {result}')
    return result

class GameRunner():
    def __init__(self, word_list, word_size = 5):
        """Initialize the game with properly-sized words."""
        self.word_list = list(filter(
            lambda w: (len(w) == word_size and w[0].islower()), word_list))

        # The list is for quick random selection; the set for quick lookup
        self.word_dict = set(self.word_list)

    def play_games(self, num_games, playerObj):
        """Play num games, return: (win rate, average num of guesses to win)."""
        num_wins = 0
        total_turns = 0
        for i in range(num_games):
            game = WordGuess(random.choice(self.word_list), self.word_dict)
            result = play_game(game, playerObj(self.word_list))
            if result != -1:
                num_wins += 1
                total_turns += result

        return (num_wins/num_games, total_turns/num_games)

