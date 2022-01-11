# Word Guess Simulator
## Description
This is a simple recreation of the "guess my word" game most recently popularized by [Wordle](https://www.powerlanguage.co.uk/wordle/). The purpose of this project is to encapsulate the game within a simple class so that simulations can be run to determine the optimal way to play it. Once that is complete, I will add some basic simulations that test different guessing strategies.

## Usage
You need a file named 'words' in your root directory. You can use your own, or on a *nix system, get one by running `cat /usr/share/dict/words > words` in the source root directory. This file will be ignored by git.

To run, use `python3 src/main.py [NUM_SIMS]`, where the argument is the number of simulations you want to run.

To see the full list of options, run `python3 src/main.py -h`.

## Output
The program will run and output the results of each game in a structure format. For instance, here is a run of 10 games, with a pretty output format:
```
 $ python3 src/main.py 10 --pretty
 Starting games...
 Output format: WINNING_WORD,NUM_TURNS_TO_WIN,[GUESS..]
 choca,6,nicky,outre,fossa,glaga,haoma,choca
 imbat,6,sepad,array,bocal,namaz,umiak,imbat
 baria,5,token,piaba,sabra,bacca,baria
 longa,-1,banig,nunch,genty,sonar,wonna,ponja
 lapel,5,mizzy,crook,snuff,label,lapel
 fuder,-1,cairn,ghost,prude,bever,duler,queer
 anode,2,snowl,anode
 chaps,6,licca,renne,booty,amaas,shaps,chaps
 ogive,6,shola,typic,buxom,knife,drive,ogive
 borty,6,arjun,yirth,dorty,sorty,rorty,borty

 NumGames: 10, Win%: 80.0, AvgTurns: 4.2
 ```

 The results are ouput in a comma-separated format. The first field is the winning word; the second field is the number of guesses it took the computer to reach it, with a -1 if it lost; the remaining fields are the guesses that the computer gave. Omitting the `--pretty` option will just print the results, without the final summary or ouput explanation.

## Acknowledgemente
Josh Wardle for the inspiration to tackle this game; check out his take on the guessing game in [this repo](https://github.com/powerlanguage/guess-my-word).

The Dartmouth Computer Science department for making me implement like three different games with this paradigm.
