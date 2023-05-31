pub struct Board {
    pub width: usize,
    pub height: usize,
}

impl Board {
    pub fn new(width: usize, height: usize) -> Board {
        Board { width, height }
    }
}
