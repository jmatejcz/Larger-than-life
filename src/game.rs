use crate::board::Board;
use crate::rules::Rules;
use pyo3::prelude::*;
use std::cmp;
#[pyclass]
pub struct Game {
    pub board: Board,
    rules: Rules,
}
impl Game {
    pub fn new(width: usize, height: usize, rules: Rules) -> Game {
        Game {
            board: Board::new(width, height),
            rules: rules,
        }
    }

    fn get_neighbours_indices(&self, row: usize, col: usize) -> Vec<(usize, usize)> {
        let mut indices: Vec<(usize, usize)> = Vec::new();
        let range: usize = self.rules.neighborhood_range;

        let start_x = col.saturating_sub(range) as usize;
        let start_y = row.saturating_sub(range) as usize;

        let end_x = cmp::min(col + range, self.board.width - 1) as usize;
        let end_y = cmp::min(row + range, self.board.height - 1) as usize;

        for x in start_x..=end_x {
            for y in start_y..=end_y {
                indices.push((x, y));
            }
        }

        indices
    }
    fn get_values_of_indices(
        &self,
        indices: Vec<(usize, usize)>,
        board_state: &Vec<Vec<f64>>,
    ) -> Vec<f64> {
        let mut values: Vec<f64> = Vec::new();
        for (x, y) in indices {
            values.push(board_state[x][y]);
        }
        values
    }
    fn verify_state(&self, current_state: f64, neighbours_values: Vec<f64>) -> f64 {
        let mut alive_count: usize = 0;
        for val in neighbours_values {
            if val == 1.0 {
                alive_count += 1;
            }
        }
        if current_state == 1.0 {
            if alive_count >= self.rules.underpopulation_limit
                && alive_count <= self.rules.overpopulation_limit
            {
                return 1.0;
            } else {
                return 0.0;
            }
        } else if alive_count == self.rules.come_alive_condition {
            return 1.0;
        } else {
            return 0.0;
        }
    }
    pub fn next_generation(&mut self, board_state: &mut Vec<Vec<f64>>) {
        for row in 0..self.board.height {
            for col in 0..self.board.width {
                let indices: Vec<(usize, usize)> = self.get_neighbours_indices(row, col);
                let values = self.get_values_of_indices(indices, board_state);
                let state = self.verify_state(board_state[col][row], values);
                board_state[col][row] = state;
            }
        }
    }
    // pub fn print_board(&self) {
    //     self.board.print()
    // }
    // pub fn get_board(&self) -> Vec<Vec<bool>> {
    //     let board = self.board.get_board().clone();
    //     board
    // }
}
