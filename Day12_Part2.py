puzzle_input = """F10
N3
F7
R90
F11"""

instructions = puzzle_input.splitlines()

#north, east, south, and west
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
current_pos = (0,0)
waypoint = (10,1)

for i in instructions:
    x,y = waypoint
    dx,dy = (0,0)
    action = i[0]
    number = int(i[1:])
    
    if action == "F":
        sx,sy = current_pos
        current_pos = (sx+x*number,sy+y*number)
        
    if action == "N":
        dx,dy = dirs[0]
        waypoint = (x+dx*number,y+dy*number)
    if action == "E":
        dx,dy = dirs[1]
        waypoint = (x+dx*number,y+dy*number)
    if action == "S":
        dx,dy = dirs[2]
        waypoint = (x+dx*number,y+dy*number)
    if action == "W":
        dx,dy = dirs[3]
        waypoint = (x+dx*number,y+dy*number)
        
    if action == "L":
        #turn waypoint counter-clockwise around ship
        turns = number//90
        for t in range(turns):
            x,y = waypoint
            waypoint = (-y,x)
        
    if action == "R":
        #turn waypoint clockwise around ship
        turns = number//90
        for t in range(turns):
            x,y = waypoint
            waypoint = (y,-x)
    
#manhattan distance

x,y = current_pos
print(abs(x) + abs(y))
