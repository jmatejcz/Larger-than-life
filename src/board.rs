pub struct Board {
    width: usize,
    height: usize,
    // true means cell alive , false - dead
    board: Vec<Vec<bool>>,
}

impl Board {
    pub fn new(width: usize, height: usize) -> Board {
        Board {
            width,
            height,
            board: vec![vec![false; width]; height],
        }
    }

    pub fn print(&self) {
        for row in &self.board {
            for val in row {
                print!("{}", if *val { 'x' } else { '.' });
            }
            println!();
        }
    }

    pub fn change_cell(&mut self, row: usize, col: usize, state: bool) {
        self.board[row][col] = state;
    }
}
