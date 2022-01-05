from game import WordGuess
from players import HumanPlayer

def play_game(game, player):
    """Play game and return the number of guesses to win, -1 if the player lost"""
    hint = ""
    while game.has_guess_left():
        guess = player.get_guess(game, hint)
        hint = game.guess_word(guess)
        if hint != "":
            print(hint)
    return game.turn if game.victory else -1

class GameRunner():
    DICTIONARY_FILE = './words'

    def __init__(self, word_size = 5):
        f = open(GameRunner.DICTIONARY_FILE, 'r')
        words_list = [ word.rstrip() for word in f.readlines() ]
        self.words_dict = { word for word in words_list if len(word) == word_size and word[0].islower()}

    def play_games(self, num_games, player):
        """Play num games and return a tuple with: (num wins, average num guesses)"""
        num_wins = 0
        total_turns = 0
        for i in range(num_games):
            game = WordGuess('tiger')
            result = play_game(game, player)
            if result != -1:
                num_wins += 1
                total_turns += result

            return (num_wins, total_turns/num_games)

# If this file is run directly, start an interactive game in the command line
if __name__ == '__main__':
    game = WordGuess('tiger')
    print('Starting a new game!')
    runner = GameRunner()
    runner.play_games(1, HumanPlayer())

