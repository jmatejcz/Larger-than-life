# Larger Than Life
An efficient `Larger Than Life` implementation combing the best of Python and Rust. [Learn more](https://conwaylife.com/wiki/Larger_than_Life)

## Installation
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
Sterowanie:
S - start. Przechodzi do ekranu gry.
R - rules. Otwiera okno pozwalające na wybór zasad gry.
P - presets. Otwiera okno wyboru ciekawych wzorów w Game of Life.
L - load. Pozwala wczytać stan gry z pliku.
H - help. Wyświetla okno pomocy.
esc - Powrót do menu głównego.
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
