# `cligames`

## Connect4 and Tic-tac-toe in the terminal
Text-based versions of Connect4 and Tic-tac-toe.

The program also contains a computer player, implemented using the minimax algorithm (with alpha–beta pruning).

Each board game can be played as human versus human, human versus computer or computer versus computer.

## Setup

#### Install via pip

```
$ pip install cligames
```

#### Build from source

```
$ git clone https://github.com/tombch/cligames.git
$ cd cligames/
$ python -m venv env
$ source env/bin/activate
$ pip install .
```

## How to play
To run the program, simply enter the following in your terminal:

```
$ cligames
```

#### Connect4
To make a move in Connect4, enter `x` when prompted, where `x` is the index of the column you wish to make a move in.

#### Tic-tac-toe
To make a move in Tic-tac-toe, input `(x, y)` when prompted, where `x` and `y` are the x and y coordinates of a square on the board.
