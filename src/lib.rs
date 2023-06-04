use pyo3::prelude::*;
use std::usize;
pub mod board;
pub mod game;
pub mod rules;

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

#[pymodule]
fn larger_than_life(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<game::Game>()?;
    m.add_function(wrap_pyfunction!(init_game, m)?)?;
    Ok(())
}
