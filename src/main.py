import logging, sys
from players import HumanPlayer, HardModeBasic
from game_runner import GameRunner

DICTIONARY_FILE = './words'

# Import and clean the words file
f = open(DICTIONARY_FILE, 'r')
word_list = [ word.rstrip() for word in f.readlines() ]
f.close()

logging.basicConfig(stream=sys.stdout, 
                    encoding='utf-8', 
                    format='[%(levelname)s] %(message)s',
                    level=logging.DEBUG)
runner = GameRunner(word_list)
result = runner.play_games(1000, HardModeBasic)
print(f'Games played: 1000, Win%: {result[0]*100}, Avg Turns: {result[1]}')
