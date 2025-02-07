advent_of_code::solution!(2);

#[derive(Copy, Clone, PartialEq, Debug)]
enum Move {
    Rock,
    Paper,
    Scissors,
}

impl Move {
    fn get_score(self) -> u64 {
        match self {
            Move::Rock => 1,
            Move::Paper => 2,
            Move::Scissors => 3,
        }
    }
    fn get_move(c: char) -> Option<Move> {
        match c {
            'X' | 'A' => Some(Move::Rock),
            'Y' | 'B' => Some(Move::Paper),
            'Z' | 'C' => Some(Move::Scissors),
            _ => None,
        }
    }
    fn get_move_from_outcome(self, outcome: char) -> Option<Move> {
        match outcome {
            'X' => match self {
                Move::Rock => Some(Move::Scissors),
                Move::Scissors => Some(Move::Paper),
                Move::Paper => Some(Move::Rock),
            },
            'Y' => Some(self), // Draw
            'Z' => match self {
                Move::Rock => Some(Move::Paper),
                Move::Scissors => Some(Move::Rock),
                Move::Paper => Some(Move::Scissors),
            },
            _ => None,
        }
    }
}

fn calculate_score(player_move: Move, opponent_move: Move) -> u64 {
    if player_move == opponent_move {
        return 3;
    } // Draw

    match (player_move, opponent_move) {
        (Move::Rock, Move::Scissors) => 6,  // Player wins
        (Move::Scissors, Move::Paper) => 6, // Player wins
        (Move::Paper, Move::Rock) => 6,     // Player wins
        _ => 0,                             // Opponent wins
    }
}

pub fn part_one(input: &str) -> Option<u64> {
    let res = input
        .lines()
        .map(|line| {
            let opponent_move =
                Move::get_move(line.chars().next().unwrap_or_default()).unwrap_or(Move::Rock);
            let player_move =
                Move::get_move(line.chars().nth(2).unwrap_or_default()).unwrap_or(Move::Rock);

            calculate_score(player_move, opponent_move) + player_move.get_score()
        })
        .sum();

    Some(res)
}

pub fn part_two(input: &str) -> Option<u64> {
    let res = input
        .lines()
        .map(|line| {
            let opponent_move =
                Move::get_move(line.chars().next().unwrap_or_default()).unwrap_or(Move::Rock);
            let outcome = line.chars().nth(2).unwrap_or_default();
            let player_move = opponent_move
                .get_move_from_outcome(outcome)
                .unwrap_or(Move::Rock);

            calculate_score(player_move, opponent_move) + player_move.get_score()
        })
        .sum();

    Some(res)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(15));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(12));
    }
}
