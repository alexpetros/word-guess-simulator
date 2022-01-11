import logging, sys, argparse
from players import HumanPlayer, HardModeBasic
from game_runner import GameRunner

DICTIONARY_FILE = './words'
RESULTS_STRING = 'NumGames: {}, Win%: {}, AvgTurns: {}'

parser = argparse.ArgumentParser(description='Run word game simulations.')
parser.add_argument('num_sims', type=int,
                    help='number of simulations to run')
# parser.add_argument('-i', metavar='word',
#                     help='initial guess for the simulation')
parser.add_argument('--debug', action='store_true', help='enable debug output')
parser.add_argument('--pretty', action='store_true',
                    help='enable pretty output and game summary')

args = parser.parse_args()

# Import and clean the words file
f = open(DICTIONARY_FILE, 'r')
word_list = [ word.rstrip() for word in f.readlines() ]
f.close()

logging.basicConfig(stream=sys.stdout,
                    encoding='utf-8',
                    format='[%(levelname)s] %(message)s',
                    level=logging.DEBUG if args.debug else logging.INFO)

if args.pretty:
    print('Starting games...')
    print('Output format: WINNING_WORD,NUM_TURNS_TO_WIN,[GUESS..]')

runner = GameRunner(word_list)
result = runner.play_games(args.num_sims, HardModeBasic)

if args.pretty:
    print()
    print(RESULTS_STRING.format( args.num_sims, result[0]*100, result[1]))
