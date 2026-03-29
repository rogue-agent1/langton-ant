#!/usr/bin/env python3
"""Langton's Ant - Simple cellular automaton producing complex behavior."""
import sys

def simulate(width=80, height=40, steps=11000):
    grid = [[0]*width for _ in range(height)]
    x, y, d = width//2, height//2, 0  # 0=up,1=right,2=down,3=left
    dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0]
    for step in range(steps):
        if grid[y][x] == 0:
            d = (d + 1) % 4; grid[y][x] = 1
        else:
            d = (d - 1) % 4; grid[y][x] = 0
        x = (x + dx[d]) % width; y = (y + dy[d]) % height
    return grid, x, y, step + 1

def render(grid):
    return "\n".join("".join("█" if c else "·" for c in row) for row in grid)

def stats(grid):
    total = sum(sum(row) for row in grid)
    return {"black_cells": total, "total": len(grid)*len(grid[0]), "density": f"{total/(len(grid)*len(grid[0]))*100:.1f}%"}

def main():
    steps = int(sys.argv[1]) if len(sys.argv) > 1 else 11000
    w = int(sys.argv[2]) if len(sys.argv) > 2 else 70
    h = int(sys.argv[3]) if len(sys.argv) > 3 else 35
    grid, fx, fy, actual = simulate(w, h, steps)
    s = stats(grid)
    print(f"=== Langton's Ant ({actual} steps) ===")
    print(f"Ant at ({fx},{fy}), {s['black_cells']} black cells ({s['density']})\n")
    print(render(grid))

if __name__ == "__main__":
    main()
