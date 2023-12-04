import os

os.chdir(r"D:\coding\advent-of-code\2023\day02")

# 12 red, 13 green, 14 blue
with open("day2.txt", "r") as f:
    lines = f.read().splitlines()

lists = [line.split(";") for line in lines]

runSum = 0
runProd = 0
def part1(game):
    colors = ["red", 'green', 'blue']
    
    colon = game[0].index(':')
    game[0] = game[0][colon+1:]
    print(game[0])

    for round in game:
        vals = [0]*3
        for token in round.split(","):
            for ind, color in enumerate(colors):
                if color in token:
                    # print(token.split()[0])
                    vals[ind] += int(token.split()[0])
            # print(vals)
            if vals[0] > 12 or vals[1] > 13 or vals[2] > 14:
                return 0
        print(vals)
    return 1

def part2(game):
    colors = ["red", 'green', 'blue']
    
    colon = game[0].index(':')
    game[0] = game[0][colon+1:]
    vals = [0]*3
    for round in game:
        for token in round.split(","):
            for ind, color in enumerate(colors):
                print(color in token)
                print(ind, color, token)
                if color in token:
                    num = int(token.split()[0])
                    vals[ind] = max(num, vals[ind])
                    print(vals[ind])
    print(vals)

    return vals[0]*vals[1]*vals[2]

for i in range(len(lists)):

    runProd += part2(lists[i])

    # if part1(lists[i]) > 0:
    #     print(f"{i+1}: " + "True")
    #     runSum += (i+1)

print(runProd)
