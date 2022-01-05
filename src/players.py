class HumanPlayer():
    def get_guess(self, game, previous_hint):
        return input(f'{game.MAX_GUESSES - game.turn} guesses left. Enter a guess:\n')

