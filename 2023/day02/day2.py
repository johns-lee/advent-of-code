import os

here = os.path.dirname(os.path.abspath(__file__))
print(here)
print(os.getcwd())
# 12 red, 13 green, 14 blue
with open("test.txt", "r") as f:
    lines = f.read().splitlines()

lists = [line.split(";") for line in lines]
print(lists)
