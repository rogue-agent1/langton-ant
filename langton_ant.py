#!/usr/bin/env python3
"""langton_ant - Langton's Ant simulation."""
import sys, argparse, json

def simulate(width, height, steps):
    grid = [[0]*width for _ in range(height)]
    x, y = width//2, height//2
    dx, dy = 0, -1
    history = []
    for step in range(steps):
        if grid[y][x] == 0:
            dx, dy = -dy, dx
            grid[y][x] = 1
        else:
            dx, dy = dy, -dx
            grid[y][x] = 0
        x = (x + dx) % width
        y = (y + dy) % height
    black = sum(sum(row) for row in grid)
    return grid, black

def render(grid):
    return "
".join("".join("█" if c else " " for c in row) for row in grid)

def main():
    p = argparse.ArgumentParser(description="Langton's Ant")
    p.add_argument("--width", type=int, default=60)
    p.add_argument("--height", type=int, default=30)
    p.add_argument("--steps", type=int, default=10000)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    grid, black = simulate(args.width, args.height, args.steps)
    if args.json:
        print(json.dumps({"width": args.width, "height": args.height, "steps": args.steps, "black_cells": black, "total_cells": args.width*args.height, "fill_pct": round(black/(args.width*args.height)*100, 1)}))
    else:
        print(render(grid))
        print(f"
{args.steps} steps, {black} black cells")

if __name__ == "__main__": main()
