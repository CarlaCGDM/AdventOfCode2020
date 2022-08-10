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

#first we change the instruction

for i in range(len(instructions)):
    
    instructions = puzzle_input.splitlines()
    
    if instructions[i][:3] == "nop":
        instructions[i] = "jmp" + instructions[i][3:]
        
    elif instructions[i][:3] == "jmp":
        instructions[i] = "nop" + instructions[i][3:]
    
    current = 0
    accumulator = 0
    visited = []
    
    #now we do the same as in part 1
    
    while True:
        
        if current in visited:
            break
        
        if current == len(instructions):
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
