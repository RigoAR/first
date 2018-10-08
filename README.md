 # 2048

Implementation of the game 2048 in python.  2048 is a single player sliding block puzzle game involving moving tiles around
a 4x4 board in the interest of making a tile with the numerical value of 2048.  The rules can be found on
www.wikihow.com/Beat-2048.  This implementation has features like save/load game, top score, and undo last move.  This
python source code has been successfully run and tested on OSX and Debian using python2.7.


<img src="https://user-images.githubusercontent.com/37717810/45250972-0d9d2680-b2f3-11e8-8a26-7f181c5c95bd.png" width=300>

Screen 1: Example starting game

<img src="https://user-images.githubusercontent.com/37717810/45250921-0a556b00-b2f2-11e8-8339-b9744aae78dc.png" width=300>

Screen 2: Saved current game to **save.txt**.

## Getting Started

To get a copy of the game from github start by cloning the jasondriver/2048 directory as follows

```
git clone https://github.com/jasondriver/2048
cd 2048
```

### Prerequisites

You will need a python interpreter on your computer and the **pygame** package.  To install pygame using pip, execute:

```
pip install pygame
```

### Running

Run the game using

```
python twenty_forty_eight.py
```

If you are on a __system with make__, just run

```
make
```

### Gameplay
Game supports both **arrow keys** and **"w", "a", "s", "d" keys** function as arrows.  When two tiles with the same number
touch, they merge into one.  Combine tiles by shifting until you reach a tile with value 2048.  

### Save/Load

In addition to saving your current game and loading it later, you can also **load** any prior game board you want as long as
it was saved by this program.

### Modifying the game

If you want to make the game harder or easier:

1. **Change the win condition** by changing the *WINNING_SCORE* variable at the top
of the twenty_forty_eight file.  

2. **Play the game with custom numbers** other than 2s and 4s by changing the numbers in the two *update()* calls in the 
*update_board()* method in the *Board* Class.
 
3. **Change the board setup on start** by changing the *board.update()* methods in *main* under the comment "# 
initialize board". 

### Running the unit tests

```
python -m unittest test_board_class.py
```

or

```
make test
```

Tests the board class's 4 shifting methods, associated methods, etc
