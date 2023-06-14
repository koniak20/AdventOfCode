import os

os.system("clear")

def first_part(output,digits):
    result = 0
    for line in output:
        for number in line:
            if len(number) == digits[1] or len(number) == digits[4] or len(number) == digits[7] or len(number) == digits[8]:
                result += 1
    return result

def sth_in_sth(first, second):
    for a in first:
        if not a in second:
            return False
    return True
def bez (first, second):
    result = ""
    for a in first:
        if not a in second:
            result += a
    return result

def second_part(output,input):
    result = 0
    tmp = ""
    for k in range(len(input)):
        try:
            line = input[k]
            line.sort(key=len)
            line = ["".join(sorted(i)) for i in line]
            tab = [1,7,4,8]
            encoded = {line[i]:tab[i] for i in range(0,3)}
            encoded["".join(sorted(line[-1]))] = 8  
            coded = {encoded[key]:key for key in encoded.keys()}
            for i in range(3,10):
                if len(line[i]) == 5:
                    if sth_in_sth(coded[1],line[i]):
                        encoded[line[i]] = 3
                        coded[3] = line[i]
                    elif sth_in_sth(bez(coded[4],coded[1]),line[i]):
                        encoded[line[i]] = 5
                        coded[5]=line[i]
                    else:
                        encoded[line[i]] = 2
                        coded[2] = line[i]
                if len(line[i]) == 6:
                    if not sth_in_sth(coded[1],line[i]):
                        encoded[line[i]] = 6
                        coded[6] = line[i]
                    elif sth_in_sth(coded[4],line[i]):
                        encoded[line[i]] = 9
                        coded[9] = line[i]
                    else:
                        encoded[line[i]] = 0
                        coded[0] = line[i]
            output[k] = [ "".join(sorted(j)) for j in output[k]]
            print(k)
            for number in output[k]:
                tmp += str(encoded[number])
            result += int(tmp)
            tmp = ""
            encoded = {}
            coded = {}
        except KeyError:
            print(output[k])
            print(input[k])
            print(encoded)
            print(coded)
    return result



if __name__ == '__main__':
    with open("/home/koniak20/Downloads/input.txt") as fuck:
        data = fuck.readlines()
        input = [] 
        output = []
        for line in data:
            tmp = line.replace("\n","").split("|")
            input.append(tmp[0].split(" ")[:-1:])
            output.append(tmp[1].split(" ")[1::])
            # print(input,"\n",output)
        digits = [6,2,5,5,4,5,6,3,7,6]  # number of parts in digits (in seven segment display)
        # print(first_part(output,digits))
        print(second_part(output,input))
        