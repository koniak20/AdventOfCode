import os

os.system("clear")

moves = [(1,0),(0,-1),(-1,0),(0,1)]

def dijikstra(graph, start, edges):
    distance = {}
    for v in graph:
        distance[v] = -1
        if v != start:
            

if __name__ == '__main__':
    with open('input_test.txt') as fuck:
        data = fuck.readlines()
        print(data)
        tab = [[int(risk) for risk in line.strip()] for line in data]
        # print(tab)
        graph = [(i%len(tab),i//len(tab[0])) for i in range(len(tab[0])*len(tab))]
        
