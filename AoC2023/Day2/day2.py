def part1():
    with open("./input2.txt") as file:
        data = file.read()
    blue = 14
    red = 12
    green = 13
    sum = 0
    possible = True
    for game in data.split('\n'):
        id = game.split(" ")[1].replace(":","")
        game = game.split(":")[1]
        for round in game.split(";"):
            if not possible:
                break
            for cubes in round.split(","):
                cubes = cubes.split(" ")[1:3]
                if cubes[1] == 'green' and int(cubes[0]) > green:
                    possible = False
                    break
                if cubes[1] == 'red' and int(cubes[0]) > red:
                    possible = False
                    break
                if cubes[1] == 'blue' and int(cubes[0]) > blue:
                    possible = False
                    break
        if possible:
            sum += int(id)
        possible = True
    print(sum)
def part2():
    with open("./input2.txt") as file:
        data = file.read()
    sum = 0
    for game in data.split('\n'):
        blue = 1
        red = 1
        green = 1
        id = game.split(" ")[1].replace(":","")
        game = game.split(":")[1]
        for round in game.split(";"):
            for cubes in round.split(","):
                cubes = cubes.split(" ")[1:3]
                if cubes[1] == 'green':
                    green = max(green,int(cubes[0]))
                if cubes[1] == 'red':
                    red = max(red,int(cubes[0]))
                if cubes[1] == 'blue':
                    blue = max(blue,int(cubes[0]))
        power = blue * red * green
        sum += power
    print(sum)



if __name__ == '__main__':
    part1()
    part2()