advent_of_code::solution!(6);
use std::collections::HashMap;

fn solve(input: &str, distinct_char_cnt: u64) -> u64{
    let mut m: HashMap<char, u64> = HashMap::new();
    let mut left = 0;
    for (i, c) in input.chars().enumerate() {
        *m.entry(c).or_insert(0) += 1;
        while m.get(&c) > Some(&1) {
            if let Some(prv) = input.chars().nth(left) {
                *m.entry(prv).or_insert(1) -= 1;
                left += 1;
            }
        }
        if (i - left + 1) as u64 == distinct_char_cnt {
            return (i+1) as u64
        }
    }
    0
}

pub fn part_one(input: &str) -> Option<u64> {
    Some(solve(&input, 4))
}

pub fn part_two(input: &str) -> Option<u64> {
    Some(solve(&input, 14))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(7));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(19));
    }
}
