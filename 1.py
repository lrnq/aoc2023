# part 1 
s = 0
for line in open('1.in'):
    digits = [int(d) for d in line if d.isdigit()]
    s += digits[0]*10 + digits[-1]
print("Part 1:", s)

# part 2
s = 0
numbers = {"one": 1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
for line in open("1.in"):
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(int(c))
        for word in numbers:
            if line[i:].startswith(word):
                digits.append(numbers[word])
    s += digits[0]*10 + digits[-1]
print("Part 2:", s)

