 # 2048

Implementation of the game 2048 in python.  Has features like save/load game and undo last move.

## Getting Started

To get a copy of the project up and running, first clone the project and enter the folder

```
git clone https://github.com/jasondriver/2048
cd 2048
```

### Prerequisites

You will need to install the **pygame** package for this project.

```
pip install pygame
```

### Running

If you are on a **system with make**, just run

```
make run menu
```
for the version with a menu or

```
make run
```
for no menu

If your system does not have make, run

```
python twenty_forty_eight.py -menu="on"
```
for the version with a menu or

```
python twenty_forty_eight.py
```
for no menu


Put menu and no menu screen shots here


## Running the tests

```
make test
```

or

```
python -m unittest test_board_class.py.py
```

### Break down of unit tests

Tests the board class's 4 shifting methods, is board full method,  etc

## Author

* **Jason Driver** 