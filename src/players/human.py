class HumanPlayer():
    def get_guess(self, game, previous_clue):
        print(previous_clue[1])
        return input(
            f'{game.MAX_GUESSES - game.turn} guesses left. Enter a guess:\n')

