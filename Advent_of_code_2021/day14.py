import os

os.system("clear")

def make_count(alphabet, polymer):
    count = {letter : 0 for letter in alphabet}
    for letter in polymer:
        count[letter] += 1
    return count

def final_answer(count):
    quantity = []
    for value in count.values():
        if value != 0:
            quantity.append(value)
    quantity.sort()
    print(quantity)
    return(quantity[-1]-quantity[0])

if __name__ == '__main__':
    with open('input.txt') as fuck:
        data = fuck.readlines()
        alphabet = list(map(chr,range(ord('A'),ord('Z')+1)))    
        polymer = data[0].strip()

        changes = {}
        for line in data[2::]:
            x,y = map(lambda x: x.strip(),line.split("->"))
            changes[x]=(x[0]+y,y+x[1])

        parts = {a:0 for a in changes.keys()}
        for ind in range(len(polymer)-1):
            parts[polymer[ind:ind+2:]] += 1

        count = make_count(alphabet,polymer)
        steps = 40
        for _ in range(steps):
            difference = {a:0 for a in changes.keys()}
            for chunk in parts.keys():
                count[changes[chunk][0][1]] += parts[chunk]
                difference[chunk] -= parts[chunk]
                difference[changes[chunk][0]] += parts[chunk]
                difference[changes[chunk][1]] += parts[chunk]
            parts = {key: parts[key] + difference[key] for key in parts.keys()}
        
        print(count)
        print(final_answer(count))
        