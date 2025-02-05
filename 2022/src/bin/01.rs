advent_of_code::solution!(1);

use std::cmp::max;

pub fn get_sum_chunk(chunk: &str) -> u64 {
    let lines = chunk.split("\n");
    let mut res: u64 = 0;
    for line in lines { res += line.parse::<u64>().unwrap_or(0); }
    res
}

pub fn part_one(input: &str) -> Option<u64> {
    let mut res: u64 = 0;
    let chunks = input.split("\n\n");

    for chunk in chunks { res = max(res, get_sum_chunk(chunk)) }
    Some(res)
}

pub fn part_two(input: &str) -> Option<u64> {
    let res = get_sum_chunk(input);
    Some(res)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(24000));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
