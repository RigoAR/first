 # 2048

Implementation of the game 2048 in python.  Has features like save/load game and undo last move.


<img src="https://user-images.githubusercontent.com/37717810/45250972-0d9d2680-b2f3-11e8-8a26-7f181c5c95bd.png" width=200>

Screen 1: Example starting game

<img src="https://user-images.githubusercontent.com/37717810/45250921-0a556b00-b2f2-11e8-8339-b9744aae78dc.png" width=200>

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

If you are on a **system with make**, just run

```
make run
```

## Running the tests

```
make test
```

or

```
python -m unittest test_board_class.py.py
```

### Break down of unit tests

Tests the board class's 4 shifting methods and associated methods

## Author

* **Jason Driver** 