use pyo3::prelude::*;
#[pyclass]
#[derive(Clone)]
pub struct Rules {
    // for now these rules are applied
    // Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure[2]).
    // Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
    // Any live cell with two or three live neighbours lives, unchanged, to the next generation.
    // Any dead cell with exactly three live neighbours will come to life.
    // Every cell interacts with its 8 neighbours
    pub underpopulation_limit: usize,
    pub overpopulation_limit: usize,
    pub come_alive_condition: usize,
    pub neighborhood_range: usize,

}

impl Rules {
    pub fn new(under_limit: usize, over_limit: usize, alive_cond: usize, nb_range: usize) -> Rules {
        Rules {
            underpopulation_limit: under_limit,
            overpopulation_limit: over_limit,
            come_alive_condition: alive_cond,
            neighborhood_range: nb_range,
        }
    }
}