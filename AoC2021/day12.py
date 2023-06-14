import os

os.system("clear")

nodes = {}
def DFS(node,visited=["start"],twice=True):
    # print(node,visited)
    result = 0
    if node == "end":
        return 1
    for next in nodes[node]:
        tmp = [] 
        if next in visited and twice and next != "start":
            result += DFS(next,visited,False)
        elif not next in visited:
            if next.lower() == next:
                tmp.append(next)
            result += DFS(next,visited+tmp,twice)
        
    return result
if __name__ == '__main__':
    with open("/home/koniak20/Desktop/Advent_of_code/Advent_of_code_2021/input_12/input.txt") as fuck:
        data = fuck.readlines()
        for line in data:
            a,b = line.strip().split("-")
            nodes[a] = nodes.get(a,[])+[b]
            nodes[b] = nodes.get(b,[])+[a]
        print(DFS("start"))
