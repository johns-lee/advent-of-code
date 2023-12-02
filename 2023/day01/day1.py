# what the fuck

with open("day1.txt", "r") as f:
    lines = f.read().splitlines()
runSum = 0
runSum2 = 0
numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def translate(line):
    for num, name in enumerate(numbers):
        line = line.replace(name, f"{name}{num}{name}")
    return line


for line in lines:
    digits = [char for char in line if char.isdigit()]
    print(digits)
    if digits:
        runSum += int(digits[0] + digits[-1])

print(runSum)

for line in lines:
    digits = [char for char in translate(line) if char.isdigit()]
    runSum2 += int(digits[0] + digits[-1])

print(runSum2)

# working attempt #1
# for i in lines:
#     temp = ""
#     for c in i:
#         if c.isdigit():
#             temp += c
#             break
#     for j in reversed(i):
#         if j.isdigit():
#             temp += j
#             break
#     runSum += int(temp)
