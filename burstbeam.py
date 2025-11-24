import heapq

def neighbors(pos, grid):
    """6-direction neighbors (x±1, y±1, z±1) in bounds and free"""
    x, y, z = pos
    X, Y, Z = len(grid), len(grid[0]), len(grid[0][0])
    nbrs = []
    for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        nx, ny, nz = x+dx, y+dy, z+dz
        if 0 <= nx < X and 0 <= ny < Y and 0 <= nz < Z:
            if grid[nx][ny][nz] == 0:
                nbrs.append((nx, ny, nz))
    return nbrs

def manhattan(p, g):
    return abs(p[0]-g[0]) + abs(p[1]-g[1]) + abs(p[2]-g[2])

def burstbeam(start, goal, grid, width=45, sub=9, delay=18):
    beams = [(manhattan(start, goal), 0, start, [start])]  # (f, depth, pos, path)
    while beams:
        candidates = []
        for _, d, pos, path in beams:
            if pos == goal:
                return path
            expand = sub if d < delay else 1
            for _ in range(expand):
                for n in neighbors(pos, grid):
                    if n not in path:  # prevent cycles
                        f = manhattan(n, goal) + d*0.001
                        candidates.append((f, d+1, n, path+[n]))
        candidates.sort(key=lambda x: x[0])
        beams = candidates[:width]
    return None
