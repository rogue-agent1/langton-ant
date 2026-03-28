#!/usr/bin/env python3
"""langton_ant - Langton's Ant simulation."""
import sys
def simulate(size=80,steps=11000):
    grid=[[0]*(size) for _ in range(size)]
    x,y=size//2,size//2;dx,dy=0,-1
    for _ in range(steps):
        if grid[y][x]==0:dx,dy=(-dy,dx);grid[y][x]=1
        else:dx,dy=(dy,-dx);grid[y][x]=0
        x=(x+dx)%size;y=(y+dy)%size
    return grid
if __name__=="__main__":
    size=int(sys.argv[1]) if len(sys.argv)>1 else 60
    steps=int(sys.argv[2]) if len(sys.argv)>2 else 11000
    grid=simulate(size,steps)
    for row in grid:print("".join("█" if c else " " for c in row))
    print(f"\n{size}x{size} grid, {steps} steps")
