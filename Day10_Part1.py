puzzle_input = """16
10
15
5
1
11
7
19
6
12
4"""

adapters = puzzle_input.splitlines()
adapters = [int(x) for x in adapters]
adapters.sort()

#start count at 1 to account for our extra adapter
    
differences = {
    3 : 1,
    2 : 0,
    1 : 0
}

joltage = 0

for adapter in adapters:
    difference = adapter - joltage
    joltage = adapter
    differences[difference] = differences[difference] + 1
    
print(differences[1]*differences[3])
