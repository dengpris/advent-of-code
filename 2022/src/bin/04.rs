advent_of_code::solution!(4);

struct Range {
    start: u64,
    end: u64,
}

impl Range {
    fn check_contained(self, other: Range) -> bool {
        (self.start >= other.start && self.end <= other.end) || (self.start <= other.start && self.end >= other.end)
    }

    fn check_overlap(self, other: Range) -> bool {
        !(self.start > other.end || self.end < other.start)
    }
}

fn get_ranges(line: &str) -> (Range, Range) {
    let mut ranges = line.split(',')
        .map(|s| {
            let mut parts = s.split('-').map(|c| c.parse::<u64>().unwrap());
            Range { start: parts.next().unwrap(), end: parts.next().unwrap() }
        });

    let first_range = ranges.next().unwrap();
    let second_range = ranges.next().unwrap();
    (first_range, second_range)
}

pub fn part_one(input: &str) -> Option<u64> {
    let res: u64 = input.lines().map(|line| {
        let (first, second) = get_ranges(line);
        first.check_contained(second) as u64
    })
    .sum();
    Some(res)
}

pub fn part_two(input: &str) -> Option<u64> {
    let res: u64 = input.lines().map(|line| {
        let (first, second) = get_ranges(line);
        first.check_overlap(second) as u64
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
        assert_eq!(result, Some(2));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(4));
    }
}
