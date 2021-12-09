import os

os.system("clear")

directions = [ (0,1), (1,0), (0,-1), (-1,0)]

def size_of_basin(area,x,y,size=0):
    area[x][y] = 9
    size += 1
    for direction in directions:
        dx,dy = direction
        if area[x+dx][y+dy] != 9:
            size = size_of_basin(area,x+dx,y+dy,size)
    return size
    


if __name__ == '__main__':
    with open("/home/koniak20/Downloads/input.txt") as fuck:
        data = fuck.readlines()
        lenght = len(data[0]) + 1
        height = len(data) + 2
        area = [[9 for _ in range(lenght)] for _ in range(height)]
        for row in range(1,height-1):
            for column in range(1,lenght-1):
                area[row][column]= int(data[row-1][column-1])
        result = 0
        basins = []
        for row in range (1,height-1):
            for column in range(1,lenght-1):
                tmp = area[row][column]
                if tmp < area[row-1][column] and tmp < area[row+1][column] and tmp < area[row][column-1] and tmp < area[row][column+1]:
                    result += tmp +1
                    basins.append((row,column))
        sizes = []
        for basin in basins:
            sizes.append(size_of_basin(area,basin[0],basin[1]))
        sizes.sort(reverse=True)
        # print(sizes)
        print(sizes[0]*sizes[1]*sizes[2])
        
