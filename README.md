# Word Guess Simulator
## Description
This is a simple recreation of the "guess my word" game most recently popularized by [Wordle](https://www.powerlanguage.co.uk/wordle/). The purpose of this project is to encapsulate the game within a simple class so that simulations can be run to determine the optimal way to play it. Once that is complete, I will add some basic simulations that test different guessing strategies.

## Usage
You need a file named 'words' in your root directory. You can use your own, or on a *nix system, get one by running `cat /usr/share/dict/words > words` in the source root directory. This file will be ignored by git.

You can run the script by either directly invoking the interpreter with `python3 src/main.py`, or using the bash wrapper, `./run-sims.sh`; these two are interchangeable. Make sure to run `chmod +x ./run-sims.sh` if you use the bash wrapper so that the shell will let you execute it directly.

To run the simulations, use `./run-sims.sh [NUM_SIMS]`.

To run the simulations with the same initial word every time, use the `--initial` option, i,e. `./run-sims.sh [NUM_SIMS] --initial spear`. Make sure that the number of characters in the initial word choice matches the number of characters in the game.

To see the full list of options, run `./run-sims.sh -h`.

## Output
The program will run and output the results of each game in a structure format. For instance, here is a run of 10 games, with the summary option at the end to tell us how the AI did:

```
$ ./run-sims.sh 10 --summary
tulsa,-1,aisle,bravo,danny,usual,fucks,gupta
toxic,4,cakes,thorn,tulip,toxic
poems,4,naics,holds,rooms,poems
psion,6,brown,icann,dozen,nylon,union,psion
haiti,5,yucca,horne,highs,habit,haiti
depts,6,shows,piers,alles,venus,debts,depts
reads,5,recap,refer,resin,realm,reads
refer,6,faust,eller,cyber,mixer,offer,refer
older,2,elder,older
boxed,5,lille,upset,warez,modem,boxed
NumGames:10, Win%:90.0, AvgTurns:4.3, InitialWord:None
 ```

The results are ouput in a comma-separated format. The first field is the winning word; the second field is the number of guesses it took the computer to reach it, with a -1 if it lost; the remaining fields are the guesses that the computer gave. Omitting the `--summary` option will just print the results of each game without the final summary.

## Acknowledgements
Josh Wardle for the inspiration to tackle this game; check out his take on the guessing game in [this repo](https://github.com/powerlanguage/guess-my-word).

The Dartmouth Computer Science department for making me implement like three different games with this paradigm.
