


if __name__ == '__main__':
    with open("/home/koniak20/Downloads/input.txt") as fuck:
        data = fuck.readline().replace("\n","").split(",")
        data = [ int(number) for number in data]
        print(data)
        n = 2000
        number_of_positions = [0]*n
        for number in data:
            number_of_positions[number] += 1
        print(number_of_positions)
        result = -1
        for i in range(0,n):
            temp = 0
            for j in range(0,i):
                temp += number_of_positions[j]*(i-j)*(i-j+1)/2
            for j in range(i,n):
                temp += number_of_positions[j]*(j-i)*(j-i+1)/2
            if result == -1:
                result = temp
            elif result > temp:
                result = temp
        print(result)