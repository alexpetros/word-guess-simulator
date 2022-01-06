# Word Guess Simulator
## Description
This is a simple recreation of the "guess my word" game most recently popularized by [Wordle](https://www.powerlanguage.co.uk/wordle/). The purpose of this project is to encapsulate the game within a simple class so that simulations can be run to determine the optimal way to play it. Once that is complete, I will add some basic simulations that test different guessing strategies.

## Usage
`python3 src/main.py` runs 1000 simulations of the game using the basic "hard mode" solver. This will be parametrized into a CLI shortly, but feel free to edit `src/main.py` in the meantime.

You need a file named 'words' in your root directory. You can use your own, or on a *nix system, get one by running `cat /usr/share/dict/words > words` in the source root directory. This file will be ignored by git.

## Acknowledgements
Josh Wardle for the inspiration to tackle this game; check out his take on the guessing game in [this repo](https://github.com/powerlanguage/guess-my-word).

The Dartmouth Computer Science department for making me implement like three different games with this paradigm.
