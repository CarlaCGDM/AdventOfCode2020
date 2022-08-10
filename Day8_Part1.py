puzzle_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

instructions = puzzle_input.splitlines()

current = 0
accumulator = 0
visited = []

while True:
    
    if current in visited:
        print(accumulator)
        break
    
    visited.append(current)
    
    instruction,number = instructions[current].split(" ")
    if instruction == "nop":
        current += 1
    if instruction == "acc":
        accumulator += int(number)
        current += 1
    if instruction == "jmp":
        current += int(number)
