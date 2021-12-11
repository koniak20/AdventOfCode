import os

os.system("clear")
n = 12
directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

def BFS (grid,x,y):

    result = 1
    que = [(x,y)]
    visited = []
    while que:
        x,y = que.pop(0)
        visited.append((x,y))
        grid[x][y] = -1
        for dir in directions:
            dx,dy = dir
            if grid[x+dx][y+dy] != -1 and not (x+dx,y+dy) in visited:
                grid[x+dx][y+dy] += 1
                if grid[x+dx][y+dy] > 9 and not (x+dx,y+dy) in que:
                    que.append((x+dx,y+dy))
                    result += 1
    return result

def show (grid):
    for line in grid:
        print(line)
def grid_add (grid):
    for row in range(1,11):
                for column in range(1,11):
                    if grid[row][column] == -1:
                        grid[row][column] += 1
                    grid[row][column] += 1
def check(grid):
    for line in grid:
        for number in line:
            if number != -1:
                return False
    return True

if __name__ == '__main__':
    with open("/home/koniak20/Downloads/input.txt") as fuck:
        data = fuck.readlines()
        data = [line.strip() for line in data]
        print(data)
        grid = [[-1]*12 for _ in range(12)]

        for row in range(1,11):
            for column in range(1,11):
                grid[row][column] = int(data[row-1][column-1])
        steps = 1000
        flashes = 0
        for _ in range(steps):
            grid_add(grid)
            for row in range(1,11):
                for column in range(1,11):
                    if grid[row][column] > 9:
                        flashes += BFS(grid,row,column)
            if check(grid):
                print("All flashed simultaneously at step : ", _+1)
                break
        print(flashes)       