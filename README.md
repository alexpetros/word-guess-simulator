# Word Guess Simulator
## Description
This is a simple recreation of the "guess my word" game most recently popularized by [Wordle](https://www.powerlanguage.co.uk/wordle/). The purpose of this project is to encapsulate the game within a simple class so that simulations can be run to determine the optimal way to play it. Once that is complete, I will add some basic simulations that test different guessing strategies.

## Usage
`python3 src/game_runner.py` runs the game with the word "tiger".

You need a file named 'words' in your root directory. You can use your own, or on a *nix system, get one by running `cat /usr/share/dict/words > words` in the source root directory. This file will be ignored by git.
