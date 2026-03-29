#!/usr/bin/env python3
"""langton_ant - Langton's Ant cellular automaton."""
import sys

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W

def simulate(steps, rule="RL"):
    grid = {}
    x, y, d = 0, 0, 0  # start at origin facing North
    path = [(x, y)]
    for _ in range(steps):
        color = grid.get((x, y), 0)
        turn = rule[color % len(rule)]
        if turn == "R":
            d = (d + 1) % 4
        elif turn == "L":
            d = (d - 1) % 4
        grid[(x, y)] = (color + 1) % len(rule)
        x += DIRS[d][0]
        y += DIRS[d][1]
        path.append((x, y))
    return grid, path

def bounds(grid):
    if not grid:
        return 0, 0, 0, 0
    xs = [x for x, y in grid]
    ys = [y for x, y in grid]
    return min(xs), min(ys), max(xs), max(ys)

def test():
    grid, path = simulate(100)
    assert len(path) == 101
    assert len(grid) > 0
    # after 10000 steps, Langton's ant creates a highway
    grid2, path2 = simulate(11000)
    assert len(path2) == 11001
    # multi-color rule
    grid3, path3 = simulate(100, "RLR")
    assert len(path3) == 101
    print("OK: langton_ant")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: langton_ant.py test")
