#!/usr/bin/env python3
"""langton_ant - Langton's Ant simulation."""
import argparse

def simulate(w, h, steps):
    grid = [[0]*w for _ in range(h)]
    x, y, d = w//2, h//2, 0  # 0=up,1=right,2=down,3=left
    dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0]
    for step in range(steps):
        if grid[y][x] == 0:
            d = (d + 1) % 4; grid[y][x] = 1
        else:
            d = (d - 1) % 4; grid[y][x] = 0
        x = (x + dx[d]) % w; y = (y + dy[d]) % h
    return grid, x, y

def main():
    p = argparse.ArgumentParser(description="Langton's Ant")
    p.add_argument("-W", "--width", type=int, default=80)
    p.add_argument("-H", "--height", type=int, default=40)
    p.add_argument("-s", "--steps", type=int, default=11000)
    args = p.parse_args()
    grid, ax, ay = simulate(args.width, args.height, args.steps)
    black = sum(sum(row) for row in grid)
    for y in range(args.height):
        print("".join("█" if grid[y][x] else " " for x in range(args.width)))
    print(f"\n{args.steps} steps, {black} black cells, ant at ({ax},{ay})")

if __name__ == "__main__":
    main()
