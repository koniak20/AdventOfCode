def part2():
    with open("./input1.txt") as file:
        input = file.readlines()
        input = [line.replace("\n","") for line in input]
        sum = 0
        numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        for line in input:
            begin = ""
            digit = ""
            digit2 = ""
            for char in line:
                begin += char
                for num in numbers:
                    if num in begin:
                        digit = str(numbers.index(num) + 1)
                        break
                if digit != "":
                    break
                if char in "0123456789":
                    digit = char
                    break
            begin = ""
            for char in line[::-1]:
                begin += char
                begin_rev = begin[::-1]
                for num in numbers:
                    if num in begin_rev:
                        digit2 = str(numbers.index(num) + 1)
                        break
                if digit2 != "":
                    break
                if char in "0123456789":
                    digit2 = char
                    break
            number = digit + digit2
            sum += int(number)
        print(sum)



def part1():
    with open("./input1.txt") as file:
        input = file.readlines()
        sum = 0
        for line in input:
            for char in line:
                if char in "0123456789":
                    digit = char
                    break
            for char in line[::-1]:
                if char in "0123456789":
                    digit2 = char
                    break
            number = digit + digit2
            sum += int(number)

    print(sum)

if __name__ == '__main__':
    part1()
    part2()