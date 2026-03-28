#!/usr/bin/env python3
"""langton_ant - Langton's Ant simulation."""
import sys
def simulate(steps, w=80, h=40):
    grid = set(); x, y = w//2, h//2; dx, dy = 0, -1
    for _ in range(steps):
        if (x, y) in grid:
            grid.discard((x, y)); dx, dy = -dy, dx  # right
        else:
            grid.add((x, y)); dx, dy = dy, -dx  # left
        x, y = (x + dx) % w, (y + dy) % h
    for r in range(h):
        print("".join("█" if (c, r) in grid else " " for c in range(w)))
    print(f"Steps: {steps} | Black cells: {len(grid)}")
if __name__ == "__main__":
    steps = int(sys.argv[1]) if len(sys.argv) > 1 else 11000
    simulate(steps)
