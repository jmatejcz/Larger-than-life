use std::usize;

use game::Game;
use numpy::ndarray::ArrayViewMut2;
use numpy::PyArrayDyn;
use pyo3::prelude::*;
mod board;
mod game;
mod rules;

#[pyfunction]
fn init_game(
    underpopulation_limit: usize,
    overpopulation_limit: usize,
    come_alive_condition: usize,
    neighborhood_range: usize,
    width: usize,
    height: usize,
) -> PyResult<PyObject> {
    Python::with_gil(|py| {
        let rules = rules::Rules::new(
            underpopulation_limit,
            overpopulation_limit,
            come_alive_condition,
            neighborhood_range,
        );
        let game = game::Game::new(width, height, rules);
        let game_py = game.into_py(py);
        Ok(game_py.into())
    })
}

#[pyfunction]
fn get_next_gen_board(game: &mut Game, board_state: &PyArrayDyn<f64>) -> PyResult<Vec<Vec<f64>>> {
    Python::with_gil(|_py| {
        let state: ArrayViewMut2<f64> = unsafe {
            board_state
                .as_array_mut()
                .into_shape((game.board.width, game.board.height))
                .unwrap()
        };
        let mut vec_array: Vec<Vec<f64>> = (0..game.board.width)
            .map(|i| (0..game.board.height).map(|j| state[[i, j]]).collect())
            .collect();

        game.next_generation(&mut vec_array);
        Ok(vec_array)
    })
}
#[pyfunction]
fn update_rules(
    game: &mut Game,
    underpopulation_limit: usize,
    overpopulation_limit: usize,
    come_alive_condition: usize,
    neighborhood_range: usize,
) -> PyResult<()> {
    game.update_rules(
        underpopulation_limit,
        overpopulation_limit,
        come_alive_condition,
        neighborhood_range,
    );
    Ok(())
}
/// A Python module implemented in Rust.
#[pymodule]
fn larger_than_life(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_next_gen_board, m)?)?;
    m.add_class::<Game>()?;
    m.add_function(wrap_pyfunction!(init_game, m)?)?;
    m.add_function(wrap_pyfunction!(update_rules, m)?)?;
    Ok(())
}
