advent_of_code::solution!(5);

use itertools::Itertools;
use std::collections::hash_map::Entry;
use std::collections::HashMap;

fn get_move(line: &str) -> (u64, u64, u64) {
    let v: Vec<u64> = line
        .split_whitespace()
        .filter_map(|s| s.parse::<u64>().ok()) // Try parsing each word as a u64
        .collect();
    (v[0], v[1], v[2])
}

fn init_stacks(input: &str) -> HashMap<u64, Vec<char>> {
    let mut stacks: HashMap<u64, Vec<char>> = HashMap::new();
    // First letter at 2nd pos, next are at +4 pos
    input.lines().for_each(|line| {
        for (i, ch) in line.chars().enumerate() {
            if i < 1 {
                continue;
            }
            let num = ((i - 1) % 4) as u64;
            if num == 0 && ch.is_alphabetic() {
                stacks
                    .entry(((i - 1) / 4 + 1).try_into().unwrap())
                    .or_insert_with(Vec::new)
                    .push(ch);
            }
        }
    });
    // Reverse the vec
    for (_, val) in stacks.iter_mut() {
        val.reverse();
    }
    stacks
}

pub fn part_one(input: &str) -> Option<String> {
    let input: Vec<&str> = input.split("\n\n").collect();
    let mut stacks: HashMap<u64, Vec<char>> = init_stacks(input[0]);
    input[1].lines().for_each(|line| {
        let (num, from, to) = get_move(line);
        for _ in 0..num {
            if let Some(value) = stacks.get_mut(&from).and_then(|vec| vec.pop()) {
                match stacks.entry(to) {
                    Entry::Occupied(mut entry) => entry.get_mut().push(value),
                    Entry::Vacant(entry) => {
                        let _ = entry.insert(vec![value]);
                    }
                }
            }
        }
    });
    let res = stacks
        .iter()
        .sorted()
        .filter_map(|(_, vec)| vec.last())
        .collect::<String>();

    Some(res)
}

pub fn part_two(input: &str) -> Option<String> {
    let input: Vec<&str> = input.split("\n\n").collect();
    let mut stacks: HashMap<u64, Vec<char>> = init_stacks(input[0]);
    input[1].lines().for_each(|line| {
        let (num, from, to) = get_move(line);
        if let Some(vec1) = stacks.get_mut(&from) {
            let subarr = vec1.split_off(vec1.len() - num as usize);
            if let Some(vec2) = stacks.get_mut(&to) {
                vec2.extend(subarr);
            }
        }
    });
    let res = stacks
        .iter()
        .sorted()
        .filter_map(|(_, vec)| vec.last())
        .collect::<String>();

    Some(res)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some("CMZ".to_string()));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
