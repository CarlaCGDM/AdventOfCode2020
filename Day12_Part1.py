puzzle_input = """F10
N3
F7
R90
F11"""

instructions = puzzle_input.splitlines()

#north, east, south, and west
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
current_dir = 1
current_pos = (0,0)

for i in instructions:
    x,y = current_pos
    dx,dy = (0,0)
    action = i[0]
    number = int(i[1:])
    if action == "F":
        dx,dy = dirs[current_dir]
    if action == "N":
        dx,dy = dirs[0]
    if action == "E":
        dx,dy = dirs[1]
    if action == "S":
        dx,dy = dirs[2]
    if action == "W":
        dx,dy = dirs[3]
    if action == "L":
        #turn left given number of degrees
        turns = number//90
        current_dir -= turns
        if current_dir < 0:
            current_dir += 4
    if action == "R":
        #turn right given number of degrees
        turns = number//90
        current_dir += turns
        if current_dir > 3:
            current_dir -= 4
        
    current_pos = (x+dx*number,y+dy*number)
    
#manhattan distance

x,y = current_pos
print(abs(x) + abs(y))
