#!/usr/bin/env python3
"""langton_ant - Langton's Ant cellular automaton simulation."""
import sys, os, time

DIRS=[(0,-1),(1,0),(0,1),(-1,0)]  # right, down, left, up

def run(w=80, h=40, steps=11000, animate=False, delay=0.01):
    grid=[[0]*w for _ in range(h)]
    x,y,d=w//2,h//2,0
    for step in range(steps):
        if grid[y][x]==0: d=(d+1)%4  # white: turn right
        else: d=(d-1)%4              # black: turn left
        grid[y][x]=1-grid[y][x]
        x=(x+DIRS[d][0])%w; y=(y+DIRS[d][1])%h
        if animate and step%100==0:
            os.system('clear')
            print(f"Step {step}")
            for row in grid: print(''.join('█' if c else ' ' for c in row))
            time.sleep(delay)
    black=sum(sum(r) for r in grid)
    if not animate:
        for row in grid: print(''.join('█' if c else ' ' for c in row))
    print(f"\n  Steps: {steps}, Black cells: {black}/{w*h} ({black/(w*h)*100:.1f}%)")

def main():
    args=sys.argv[1:]
    steps=int(args[0]) if args and args[0].isdigit() else 11000
    w=int(args[args.index('-w')+1]) if '-w' in args else 80
    h=int(args[args.index('-h')+1]) if '-h' in args else 40
    animate='--animate' in args
    run(w, h, steps, animate)

if __name__=='__main__': main()
