 # 2048

Implementation of the game 2048 in python.  Has features like save/load game and undo last move.  Tested and working on 
OSX and Debian using python2.7.


<img src="https://user-images.githubusercontent.com/37717810/45250972-0d9d2680-b2f3-11e8-8a26-7f181c5c95bd.png" width=300>

Screen 1: Example starting game

<img src="https://user-images.githubusercontent.com/37717810/45250921-0a556b00-b2f2-11e8-8339-b9744aae78dc.png" width=300>

Screen 2: Saved current game to **save.txt**.

## Getting Started

To get a copy of the project up and running, first clone the project and enter the folder

```
git clone https://github.com/jasondriver/2048
cd 2048
```

### Prerequisites

You will need the **pygame** package for this project.  To install:

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
Game supports both **arrow keys** and **wasd keys**.  Combine tiles by shifting until you reach a tile with value 2048.  

In addition to saving your current game and loading it later, you can also load any game board you want as long as
it is the correct format using **Load**.  See the correct format by using the **Save** button and looking at save.txt.

If you want to make the game harder:

1. **Change the win condition** by changing the *WINNING_SCORE* variable at the top
of the twenty_forty_eight file.  

2. **Play the game with custom numbers** other than 2s and 4s by changing the numbers in the two *update()* calls in the 
*update_board()* method in the *Board* Class.
 
3. **Change the board setup on start** by changing the *board.update()* methods in *main* under the comment "# 
initialize board". 

### Running the tests

```
python -m unittest test_board_class.py.py
```

or

```
make test
```

### Break down of unit tests

Tests the board class's 4 shifting methods and associated methods
