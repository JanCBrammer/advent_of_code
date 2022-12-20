"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit;
his elves have provided him the distances between every pair of locations.
He can start and end at any two (different) locations he wants,
but he must visit each location exactly once.
What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605,
and so the answer is 605 in this example.

What is the distance of the shortest route?

--- Part Two ---

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants,
and he still must visit each location exactly once.

For example, given the distances above,
the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

--- Notes ---

- https://en.wikipedia.org/wiki/Travelling_salesman_problem
- list all Hamiltonian paths (not cycles!) and select the one with the lowest total weight
- https://en.wikipedia.org/wiki/Hamiltonian_path
- since the graph is complete / fully connected, and small, brute force will do:
    find permutation of cities that yields the shortest/longest path
"""
import itertools
from collections import defaultdict
from pathlib import Path


def parse_input(input_path: str) -> dict[str, dict[str, int]]:

    city_distances = defaultdict(dict)

    with Path(input_path).open() as file:
        for line in file:

            cities, distance = line.split("=")
            distance = int(distance.strip())
            city1, city2 = (city.strip() for city in cities.split("to"))

            city_distances[city1].update({city2: distance})
            city_distances[city2].update({city1: distance})

    return city_distances


def compute_path_length(
    cities: list[str], city_distances: dict[str, dict[str, int]]
) -> int:

    path_length = 0

    for city1, city2 in itertools.pairwise(cities):
        path_length += city_distances[city1][city2]

    return path_length


def find_extreme_path(
    city_distances: dict[str, dict[str, int]],
    initial_extreme: float,
    decision_function: callable,
) -> int:

    extreme_path = initial_extreme

    for path in itertools.permutations(city_distances.keys()):
        extreme_path = decision_function(
            compute_path_length(path, city_distances), extreme_path
        )

    return extreme_path


def solve_part1(input_path: str):

    city_distances = parse_input(input_path)
    shortest_path = find_extreme_path(city_distances, float("inf"), min)

    print(f"Part 1:\nSanta, the shortest route is {shortest_path} long!\n")


def solve_part2(input_path: str):

    city_distances = parse_input(input_path)
    longest_path = find_extreme_path(city_distances, float("0"), max)

    print(f"Part 2:\nSanta, the longest route is {longest_path} long!\n")


if __name__ == "__main__":

    solve_part1(f"{Path(__file__).parts[-2]}/input.txt")
    solve_part2(f"{Path(__file__).parts[-2]}/input.txt")
