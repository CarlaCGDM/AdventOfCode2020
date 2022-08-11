puzzle_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

rows = puzzle_input.splitlines()
grid = []
for row in rows:
    grid.append(list(row))
    
def adjacent_positions(seat:tuple,grid):
    adjacents = []
    y,x = seat
    dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    for d in dirs:
        yd,xd = d
        if y+yd in range(len(grid)) and x+xd in range(len(grid[0])):
            adjacents.append((y+yd,x+xd))
            
    return(adjacents)
    
def count_seats(seat:tuple,grid,character):
    seats = 0
    adjacents = adjacent_positions(seat,grid)
    for position in adjacents:
        y,x = position
        if grid[y][x] == character:
            seats += 1
    return seats

#if all seats around an empty seat are empty, it becomes taken
#if four or more seats around a taken seat are taken, it becomes empty
    
loop = 0
height = len(grid)
width = len(grid[0])

while True:
    
    flipped = []
    
    for i in range(height):
        for j in range(width):
            seat = grid[i][j]
            if seat == "L":
                if count_seats((i,j),grid,"#") == 0:
                    flipped.append((i,j))
            if seat == "#":
                if count_seats((i,j),grid,"#") >= 4:
                    flipped.append((i,j))
    
    for seat in flipped:
        y,x = seat
        if grid[y][x] == "L":
            grid[y][x] = "#"
        elif grid[y][x] == "#":
            grid[y][x] = "L"
            
    if len(flipped) == 0:
        break
    else:
        loop += 1
        
result = 0
for row in grid:
    for seat in row:
        if seat == "#":
            result += 1
            
print(result)
