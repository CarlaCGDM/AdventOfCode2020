puzzle_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

import operator

parsedinput = puzzle_input.splitlines()

#passwords with their restricted letter and their min/max

passwords = []

for line in parsedinput:
    data = line.split()
    password = data[2]
    letter = data[1][0]
    numbers = data[0].split('-')
    pos1 = int(numbers[0]) - 1
    pos2 = int(numbers[1]) - 1
    passwords.append([password,letter,pos1,pos2])

    
correct_passwords = 0

for p in passwords:
    if operator.xor(p[0][p[2]] == p[1], p[0][p[3]] == p[1]):
        correct_passwords += 1
        
print(correct_passwords)
