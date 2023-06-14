import os

os.system("clear")

symbol = "0"
def folding_x (fold,paper,x,y):
    for col in range(fold+1,x):
            for row in range(y):
                if paper[row][col] == symbol:
                    paper[row][2*fold - col] = symbol
def folding_y (fold,paper,x,y):
    for row in range(fold+1,y):
            for col in range(x):
                if paper[row][col] == symbol:
                    paper[2*fold - row][col] = symbol

if __name__ == '__main__':
    with open('input.txt') as fuck:
        data = fuck.readlines()
        x,y = 0,0
        dots = []
        instructions = []
        for line in data:
            if line[:4:] == "fold":
                a,b = (line.strip().split()[-1].split("="))
                instructions.append((a,b))
            else:
                a,b = (line.strip().split(","))
                a,b = int(a),int(b)
                x,y = max(x,a+1),max(y,b+1)
                dots.append((a,b))
        how_many = len(instructions)
        paper = [[" "]*x for _ in range(y)]
        for dot in dots:
            a,b = dot
            paper[b][a]=symbol
        for instr in instructions[:how_many]:
            a,b = instr
            b = int(b)
            if a == "y":
                folding_y(b,paper,x,y)
                y = b
            else:
                folding_x(b,paper,x,y)
                x = b
        result = 0
        for row in range(y):
            for col in range(x):
                if paper[row][col] == symbol:
                    result += 1
        print(result)
        for line in paper[:y]:
            t=""
            for a in line[:x]:
                t+=a
            print(t)