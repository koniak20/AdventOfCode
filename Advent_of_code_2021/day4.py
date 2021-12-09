from os import EX_OSFILE


if __name__ == '__main__':
    with open("/home/koniak20/Downloads/input.txt") as fuck:
        data = fuck.readlines()
        n = 1000
        row = [0]*n
        table = [ [0]*n for _ in range(n)]

        
        for line in data:
            line=line.replace(" -> ",",").replace("\n","").split(",")
            line = [int(a) for a in line]
            # print(line)
            if line[0] == line[2]:
                if line[1] > line[3]:
                    line[1],line[3] = line[3],line[1]
                for i in range(line[1],line[3]+1):
                    # print(i)
                    table[i][line[0]] += 1
            elif line[1] == line[3]:
                if line[0] > line[2]:
                    line[0] , line[2] = line[2] , line[0]
                for i in range(line[0],line[2]+1):
                    table[line[1]][i] += 1
            else :
                x_change = 0
                y_change = 0
                if line[0] > line[2]:
                    x_change = -1
                else:
                    x_change = 1
                if line[1] > line[3]:
                    y_change = -1
                else:
                    y_change = 1
                for i in range(abs(line[0]-line[2])+1):
                    table[line[1]+i*y_change][line[0]+i*x_change] +=1
        # for l in table:
        #             print(l)       
        result = 0
        # print(table)
        for row in range(n):
            for column in range(n):
                if table[row][column] > 1:
                    result += 1

        print(result)
        # print(data)