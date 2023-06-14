from os import EX_OSFILE


if __name__ == '__main__':
    with open("/home/koniak20/Downloads/input.txt") as fuck:
        data = fuck.readline().replace("\n","").split(",")
        print(data)
        fishes = [0] * 9
        days = 256
        for number in data:
            fishes[int(number)] += 1
        print(fishes)
        for _ in range(days):
            zeros = fishes[0]
            fishes = [fishes[(i+1)%9] for i in range(9) ]
            fishes[6] += zeros
            # print(fishes)
        print(fishes)
        result = 0
        for i in fishes:
            result += i
        print(result)
        