if __name__ == '__main__':
    with open("/home/koniak20/Downloads/input_1.txt") as fuck:
        order = fuck.readline()
        order = order.replace("\n","").split(",")
        # print(order)
        data = fuck.readlines()
        # print(data[:5])
        table = [[5]*6]*6
        tables = []
        index = 1
        sum = 0
        for line in data:
            if line != "\n":
                table[index]=[5]+line.split()
                index += 1
            elif index == 6:
                tables.append(table)
                table = [[5]*6]*6
                index = 1
        tables.append(table)
        # for table in tables:
        #     for row in table:
        #         print(row)
        #     print("\n")
        winners = -1
        # print(order)
        boolik = False
        won =[0]*len(tables)
        for number in order:
            for table in range(len(tables)):
                for column in range(1,6):
                    for row in range(1,6):
                        if tables[table][row][column] == number:
                            # print("Number :", number ,"Row: ",row, " column: ", column, " table: ", table)
                            tables[table][row][column] = -1
                            tables[table][0][column] -= 1
                            tables[table][row][0] -= 1
                            if won[table] == 0 and (tables[table][row][0] == 0 or tables[table][0][column] == 0):
                                winners = table
                                won[table] = 1
                                boolik = True
            if boolik:
                sum =0  
                print(number, winners)
                for column in range(1,6):
                    for row in range(1,6):
                        if tables[winners][row][column] != -1:
                            sum += int(tables[winners][row][column])
                boolik = False
        print(sum*21)
        # for table in tables:
        #     for row in table:
        #         print(row)
        #     print("\n")
