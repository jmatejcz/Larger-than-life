# Larger Than Life
An efficient `Larger Than Life` implementation combing the best of Python and Rust. [Learn more](https://conwaylife.com/wiki/Larger_than_Life)

## Installation
Minimal python versin required is Python3.10.
We recommend setting up virtual environment for a clean install and easy development.\
`python -m venv env`

**Environment activation**\
Windows: `env\Scripts\activate.bat`\
Linux:  `source env/bin/activate`

**Package installation**\
`pip install -r "requirements.txt"`

## Build
To build the project simply run `maturin develop` in project directory.

**To run the application:**\
go to larger-than-life-app/ folder
and run:
`python app.py`
to start a game
## Guide / How to play
Controls:
S - start. Go to game screen.
R - rules. Opens window allowing to change rules.
P - presets. Opens window to choose interesting patterns.
L - load. Allows loading game state from file.
H - help. Opens help window.
esc - escaping to menu screen.
## Test
To run Rust unit tests:\
`cargo test`

## Docs 
To generate automatic documenation for rust code:\
`cargo doc`

It will generate htmls with documentation

For python code:
`sphinx-build -b html docs/source/ docs/build/html/`


## Authors and acknowledgment
Jan Rybarczyk & Jakub Matejczyk
