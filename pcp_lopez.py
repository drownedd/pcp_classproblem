# Christian Lopez García
# Found solution for Exercise 40: abbaabbabaabaababbaabbaabbabaabbabaabaabbabaabaababbaaabaababbababaabaababaabaabaababbaabbaaababaabbabaabaabbaaabaababbaaabaababaabaababaababaabbaaabaabab
# indexes (0, 3]: [1, 3, 2, 3, 3, 1, 0, 1, 3, 2, 3, 2, 3, 3, 2, 3, 3, 1, 0, 3, 3, 1, 0, 2, 3, 0, 0, 2, 3, 3, 3, 1, 0, 1, 0, 0, 0, 2, 3, 2, 3, 0, 1, 0, 3, 3, 1, 0, 3, 0, 0, 2, 3, 0, 0, 2, 0, 0, 2, 0, 1, 0, 3, 0, 0, 2]

from collections import deque

A = ["aab", "ab", "ab", "ba"]
B = ["a", "abb", "bab", "aab"]

TEST_1 = ["1", "10111", "10"]
TEST_2 = ["111", "10", "0"]

l1 = A
l2 = B


class Node:
    def __init__(self, word_1: str, word_2: str, indexes: list[int]) -> None:
        self.word_1 = word_1
        self.word_2 = word_2
        self.indexes = indexes

    def __eq__(self, __value: object) -> bool:
        return self.word_1 == __value.word_1 and self.word_2 == __value.word_2

    def __str__(self) -> str:
        return self.word_1 + ", " + self.word_2 + ", " + str(self.indexes)

    def __hash__(self) -> int:
        return hash((self.word_1, self.word_2))

    def get_neighbours(self) -> list['Node']:
        neighbours = []
        for i, (word_1, word_2) in enumerate(zip(l1, l2)):
            new_word_1 = self.word_1 + word_1
            new_word_2 = self.word_2 + word_2
            if new_word_1.startswith(new_word_2) or new_word_2.startswith(new_word_1):
                neighbours.append(
                    Node(self.word_1 + word_1, self.word_2 + word_2, indexes=[*self.indexes + [i]]))
        return neighbours

    def is_solution(self) -> bool:
        return self.word_1 == self.word_2


def solve() -> list[int]:
    """BFS naive algorithm to get a solution with the given word lists"""
    starting_node = Node("", "", [])

    fringe = deque([starting_node])
    visited = set([starting_node])

    while fringe:
        for neighbour in fringe.popleft().get_neighbours():
            if neighbour not in visited:
                if neighbour.is_solution():
                    return neighbour.indexes
                fringe.append(neighbour)
                visited.add(neighbour)


def print_sol(sol: list[int]):
    if not sol:
        print("! No solution found")
    word_1 = word_2 = ""
    for i in sol:
        word_1 += l1[i]
        word_2 += l2[i]
    print(f"{word_1} = {word_2}, {sol}")


if __name__ == "__main__":
    sol = solve()
    print_sol(sol)
