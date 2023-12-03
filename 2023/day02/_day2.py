import os

# os.chdir(r"D:\coding\adventofcode_2023\day02")

# 12 red, 13 green, 14 blue
with open("test.txt", "r") as f:
    lines = f.read().splitlines()

lists = [line.split(";") for line in lines]
print(lists)
