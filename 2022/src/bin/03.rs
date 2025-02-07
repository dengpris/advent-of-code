use itertools::Itertools;
use std::collections::HashSet;
advent_of_code::solution!(3);

fn get_value(c: char) -> u64 {
    if c.is_ascii_lowercase() {
        c as u64 - 'a' as u64 + 1
    } else {
        c as u64 - 'A' as u64 + 27
    }
}

pub fn part_one(input: &str) -> Option<u64> {
    let res = input
        .lines()
        .map(|line| {
            let (first, second) = line.split_at(line.len() / 2);
            let a = first.chars().collect::<HashSet<_>>();
            let b = second.chars().collect::<HashSet<_>>();
            a.intersection(&b).copied().map(get_value).sum::<u64>()
        })
        .sum();
    Some(res)
}

pub fn part_two(input: &str) -> Option<u64> {
    let res = input
        .lines()
        .chunks(3)
        .into_iter()
        .map(|chunk| {
            let (a, b, c) = chunk.collect_tuple().unwrap();
            let a = a.chars().collect::<HashSet<_>>();
            let b = b.chars().collect::<HashSet<_>>();
            let c = c.chars().collect::<HashSet<_>>();
            a.iter()
                .filter(|ch| b.contains(ch) && c.contains(ch))
                .copied()
                .map(get_value)
                .sum::<u64>()
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
        assert_eq!(result, Some(157));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(70));
    }
}
