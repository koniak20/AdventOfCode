import os

os.system("clear")

if __name__ == '__main__':
    with open("/home/koniak20/Downloads/input.txt") as fuck:
        data = fuck.readlines()
        # print(data)
        stack = []
        boolik = True
        tab = ["[","<","{","("]
        fir = {"[":"2","<":"4","{":"3","(":"1"}
        sec = {"]":"[",">":"<","}":"{",")":"("}
        result = 0
        scores = []
        score = 0
        for line in data:
            for char in line.replace("\n",""):
                # print(stack)
                if char in tab:
                    stack.append(char)
                else:
                    if stack[-1] == sec[char]:
                        stack.pop()
                    else:
                        if char == ")":
                            result += 3
                        elif char == "]":
                            result += 57
                        elif char == "}":
                            result+= 1197
                        elif char == ">":
                            result+= 25137
                        boolik = False
                        break
            if boolik:
                while len(stack) >0:
                    score *= 5
                    k = stack[-1]
                    score += int(fir[k])
                    stack.pop()
                scores.append(score)
                score = 0
            boolik = True
            stack.clear()
            # print(result)
        scores.sort()
        print(scores[int(len(scores)/2)])