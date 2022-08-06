puzzle_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

parsedinput = puzzle_input.splitlines()

#store passwords with their restricted letter and their min/max

passwords = []

for line in parsedinput:
    data = line.split()
    password = data[2]
    letter = data[1][0]
    numbers = data[0].split('-')
    minimum = numbers[0]
    maximum = numbers[1]
    passwords.append([password,letter,minimum,maximum])
    
    
correct_passwords = 0

for p in passwords:
    if p[0].count(p[1]) in range(int(p[2]),int(p[3])+1):
        correct_passwords += 1
        
print(correct_passwords)
