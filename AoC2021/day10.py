import os

os.system("clear")

if __name__ == '__main__':
    with open("./input_10/input_test.txt") as fuck:
        data = fuck.readlines()
        fir = {"[":2,"<":4,"{":3,"(":1}
        sec = {"]":"[",">":"<","}":"{",")":"("}
        points = {')': 3, ']': 57, '}': 1197, '>': 25137}
        result = 0
        scores = []
        for line in data:
            stack = []
            for char in line.strip():
                if char in sec.values():
                    stack.append(char)
                elif not stack or stack.pop() != sec[char]:
                    result += points[char]
                    stack = []
                    break
            if stack:
                score = 0
                while len(stack) >0:
                    score = 5*score + fir[stack[-1]]
                    stack.pop()
                scores.append(score)
            # print(result)
        scores.sort()
        print(scores[int(len(scores)/2)])