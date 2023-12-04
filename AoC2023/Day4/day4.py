
def part1():
    with open("input4.txt") as file:
        input = file.read()
    result = 0
    cards = input.split("\n")
    for card in cards:
        points = 0
        winning_numbers = card.split(":")[1].split("|")[0]
        numbers = card.split(":")[1].split("|")[1].split(" ")
        while "" in numbers:
            numbers.remove("")
        for number in numbers:
            if number in winning_numbers.split(" "):
                points +=1
        if points != 0:
            result += pow(2, points - 1)
    print(result)

def part2():
    with open("input4.txt") as file:
            input = file.read()
    result = 0
    cards = input.split("\n")
    cards_numbers = [1 for _ in range(len(cards))]
    for i,card in enumerate(cards):
        points = 0
        winning_numbers = card.split(":")[1].split("|")[0]
        numbers = card.split(":")[1].split("|")[1].split(" ")
        while "" in numbers:
            numbers.remove("")
        for number in numbers:
            if number in winning_numbers.split(" "):
                points +=1
        for j in range(i+1,i+points+1):
            cards_numbers[j] += cards_numbers[i]
    print(sum(cards_numbers))

if __name__ == '__main__':
    part1()
    part2()