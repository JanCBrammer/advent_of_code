"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds,
but must rest occasionally to recover their energy.
Santa would like to know which of his reindeer is fastest,
and so he has them race.

Reindeer can only either be flying (always at their top speed)
or resting (not moving at all),
and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

- Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
- Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
After one second, Comet has gone 14 km, while Dancer has gone 16 km.
After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km.
On the eleventh second, Comet begins resting (staying at 140 km),
and Dancer continues on for a total distance of 176 km.
On the 12th second, both reindeer are resting.
They continue to rest until the 138th second,
when Comet flies for another ten seconds.
On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting,
and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point).
So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds,
what distance has the winning reindeer traveled?

--- Part Two ---

Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead.
(If there are multiple reindeer tied for the lead, they each get one point.)
He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second,
Dancer is in the lead and gets one point.
He stays in the lead until several seconds into Comet's second burst:
after the 140th second, Comet pulls into the lead and gets his first point.
Of course, since Dancer had been in the lead for the 139 seconds before that,
he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet,
our old champion, only has 312. So, with the new scoring system,
Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input),
after exactly 2503 seconds, how many points does the winning reindeer have?



--- Notes ---

"""
from pathlib import Path


def parse_input(input_path: str) -> dict[str, dict[str, int]]:
    reindeer_performance_data = {}

    with Path(input_path).open() as file:
        for line in file:
            split_line = line.strip().split()
            reindeer_performance_data[split_line[0]] = {
                "go_distance_per_time": int(split_line[3]),
                "go_time": int(split_line[6]),
                "rest_time": int(split_line[13]),
            }

    return reindeer_performance_data


def compute_covered_distance(race_time: int, performance_data: dict[str, int]) -> int:
    go_time = performance_data["go_time"]
    rest_time = performance_data["rest_time"]
    go_distance_per_time = performance_data["go_distance_per_time"]

    quotient, remainder = divmod(
        race_time,
        go_time + rest_time,
    )

    distance = quotient * go_time * go_distance_per_time
    distance += min(go_time, remainder) * go_distance_per_time

    return distance


def compute_winning_distance(
    race_time: int, reindeer_performance_data: dict[str, dict[str, int]]
) -> int:
    max_distance = 0

    for performance_data in reindeer_performance_data.values():
        distance = compute_covered_distance(race_time, performance_data)
        if distance > max_distance:
            max_distance = distance

    return max_distance


def compute_winning_points(
    race_time: int, reindeer_performance_data: dict[str, dict[str, int]]
) -> int:
    race_points = dict(
        zip(reindeer_performance_data.keys(), [0] * len(reindeer_performance_data))
    )

    for race_second in range(race_time):
        distances = {}
        for reindeer, performance_data in reindeer_performance_data.items():
            distances[reindeer] = compute_covered_distance(
                race_second + 1, performance_data
            )
        winning_distance = max(distances.values())
        for reindeer, distance in distances.items():
            if distance == winning_distance:
                race_points[reindeer] += 1

    return max(race_points.values())


def solve_part1(input_path: str):
    reindeer_performance_data = parse_input(input_path)
    max_distance = compute_winning_distance(2503, reindeer_performance_data)

    print(
        f"Part 1:\nThe winning reindeer covered {max_distance} km after 2503 seconds.\n"
    )


def solve_part2(input_path: str):
    reindeer_performance_data = parse_input(input_path)
    max_points = compute_winning_points(2503, reindeer_performance_data)

    print(
        f"Part 2:\nThe winning reindeer won {max_points} points after 2503 seconds.\n"
    )


if __name__ == "__main__":
    solve_part1(f"{Path(__file__).parent}/input.txt")
    solve_part2(f"{Path(__file__).parent}/input.txt")
