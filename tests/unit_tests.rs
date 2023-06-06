#[cfg(test)]
mod tests {
    use larger_than_life::game::Game;
    // use larger_than_life::rules::Rules;

    #[test]
    fn get_neighbours_indices_middle_point() {
        let game: Game = Game::new_default_rules(3, 3);
        let result = game.get_neighbours_indices(1, 1);
        let target: Vec<(usize, usize)> = vec![
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 1),
            (2, 1),
            (0, 2),
            (1, 2),
            (2, 2),
        ];
        assert_eq!(result, target)
    }

    #[test]
    fn get_neighbours_indices_first_row_point() {
        let game: Game = Game::new_default_rules(3, 3);
        let result = game.get_neighbours_indices(0, 1);
        let target: Vec<(usize, usize)> = vec![(0, 0), (2, 0), (0, 1), (1, 1), (2, 1)];
        assert_eq!(result, target)
    }

    #[test]
    fn get_neighbours_indices_last_row_point() {
        let game: Game = Game::new_default_rules(3, 3);
        let result = game.get_neighbours_indices(2, 1);
        let target: Vec<(usize, usize)> = vec![(0, 1), (1, 1), (2, 1), (0, 2), (2, 2)];
        assert_eq!(result, target)
    }

    #[test]
    fn get_neighbours_indices_first_point() {
        let game: Game = Game::new_default_rules(3, 3);
        let result = game.get_neighbours_indices(0, 0);
        let target: Vec<(usize, usize)> = vec![(1, 0), (0, 1), (1, 1)];
        assert_eq!(result, target)
    }

    #[test]
    fn get_neighbours_indices_last_point() {
        let game: Game = Game::new_default_rules(3, 3);
        let result = game.get_neighbours_indices(2, 2);
        let target: Vec<(usize, usize)> = vec![(1, 1), (2, 1), (1, 2)];
        assert_eq!(result, target)
    }

    #[test]
    fn get_values_of_indices_test() {
        let game: Game = Game::new_default_rules(3, 3);
        let indices: Vec<(usize, usize)> = vec![(0, 1), (1, 1), (2, 1), (0, 2), (2, 2)];
        let board_state: &Vec<Vec<f64>> = &vec![
            vec![0.0, 0.0, 1.0],
            vec![1.0, 0.0, 1.0],
            vec![0.0, 1.0, 1.0],
        ];
        let result: Vec<f64> = game.get_values_of_indices(indices, board_state);
        let target: Vec<f64> = vec![0.0, 0.0, 1.0, 1.0, 1.0];
        assert_eq!(result, target)
    }

    #[test]
    fn verify_state_alive_stay_alive_test() {
        let game: Game = Game::new_default_rules(3, 3);
        let neighbours_values: Vec<f64> = vec![0.0, 0.0, 1.0, 1.0, 1.0];
        let result: f64 = game.verify_state(1.0, neighbours_values);
        let target: f64 = 1.0;
        assert_eq!(result, target)
    }

    #[test]
    fn verify_state_alive_go_dead_from_underpop_test() {
        let game: Game = Game::new_default_rules(3, 3);
        let neighbours_values: Vec<f64> = vec![0.0, 0.0, 0.0, 0.0, 1.0];
        let result: f64 = game.verify_state(1.0, neighbours_values);
        let target: f64 = 0.0;
        assert_eq!(result, target)
    }

    #[test]
    fn verify_state_alive_go_dead_from_overpop_test() {
        let game: Game = Game::new_default_rules(3, 3);
        let neighbours_values: Vec<f64> = vec![1.0, 1.0, 1.0, 0.0, 1.0];
        let result: f64 = game.verify_state(1.0, neighbours_values);
        let target: f64 = 0.0;
        assert_eq!(result, target)
    }

    #[test]
    fn verify_state_dead_stay_dead_test() {
        let game: Game = Game::new_default_rules(3, 3);
        let neighbours_values: Vec<f64> = vec![0.0, 0.0, 0.0, 1.0, 1.0];
        let result: f64 = game.verify_state(1.0, neighbours_values);
        let target: f64 = 1.0;
        assert_eq!(result, target)
    }

    #[test]
    fn verify_state_dead_go_alive_test() {
        let game: Game = Game::new_default_rules(3, 3);
        let neighbours_values: Vec<f64> = vec![0.0, 0.0, 1.0, 1.0, 1.0];
        let result: f64 = game.verify_state(0.0, neighbours_values);
        let target: f64 = 1.0;
        assert_eq!(result, target)
    }
}
