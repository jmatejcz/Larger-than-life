use crate::board::Board;
use crate::rules::Rules;

pub struct Game {
    pub board: Board,
    game_over: bool,
    rules: Rules,
}
impl Game {
    pub fn new(width: usize, height: usize) -> Game {
        Game {
            board: Board::new(width, height),
            game_over: false,
            rules: Rules::new(),
        }
    }

    pub fn next_generation(&mut self) {}
    pub fn print_board(&self) {
        self.board.print()
    }
}
