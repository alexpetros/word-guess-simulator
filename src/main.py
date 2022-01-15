import logging, sys, argparse
from players.random_guess import RandomGuessHardMode
from game_runner import GameRunner

DICTIONARY_FILE = './resources/words'
RESULTS_STRING = 'NumGames:{}, Win%:{}, AvgTurns:{}, InitialWord:{}'
DEFAULT_LENGTH = 5

# Define command line options
parser = argparse.ArgumentParser(prog='run-sims',
                                 description='Run word game simulations.')
parser.add_argument('num_sims', type=int,
                    help='number of simulations to run')
parser.add_argument('-d', '--dictionary', metavar='FILEPATH',
                    help='dictionary of words to use for the game')
parser.add_argument('-i', '--initial',  metavar='WORD',
                    help='initial guess for each game')
parser.add_argument('-q', '--quiet', action='store_true',
                    help='suppress output of individual games')
parser.add_argument('--word-length', metavar='NUM',
                    help='the length of the word to guess')
parser.add_argument('-s', '--summary', action='store_true',
                    help='print game summary in final line')
parser.add_argument('--debug', action='store_true', help='enable debug output')
args = parser.parse_args()

# Import and clean the words file
fp = args.dictionary if args.dictionary is not None else DICTIONARY_FILE
f = open(fp, 'r')
word_list = [ word.rstrip() for word in f.readlines() ]
f.close()

# Set up logging
logging.basicConfig(stream=sys.stdout,
                    encoding='utf-8',
                    format='[%(levelname)s] %(message)s',
                    level=logging.DEBUG if args.debug else logging.INFO)

# Validate initial word
word_length = args.word_length if args.word_length != None else DEFAULT_LENGTH
if args.initial:
    if len(args.initial) != word_length:
        raise Exception('Length of initial word does not match game length.')
    if args.initial not in word_list:
        raise Exception(f'Initial word {args.initial} not found in dictionary')

show_games = not args.quiet
runner = GameRunner(word_list, 5, show_games=show_games)
result = runner.play_games(args.num_sims, RandomGuessHardMode, initial=args.initial)

if args.summary:
    print(RESULTS_STRING.format(args.num_sims, result[0]*100, result[1],
                                args.initial))
