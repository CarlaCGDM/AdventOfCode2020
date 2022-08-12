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
    
#modify count function to keep looking in a direction until something is found
    
def count_seats(seat:tuple,grid,character):
    count = 0
    ys,xs = seat
    dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    for d in dirs:
        yd,xd = d
        y = ys+yd
        x = xs+xd
        while y in range(len(grid)) and x in range(len(grid[0])):
            if grid[y][x] != "." and grid[y][x] != character:
                break
            if grid[y][x] == character:
                count += 1
                break
            y+=yd
            x+=xd
            
    return(count)

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
                if count_seats((i,j),grid,"#") >= 5:
                    flipped.append((i,j))
    
    for seat in flipped:
        y,x = seat
        if grid[y][x] == "L":
            grid[y][x] = "#"
        elif grid[y][x] == "#":
            grid[y][x] = "L"
            
    if len(flipped) == 0:
        break
    
    loop += 1
        
result = 0
for row in grid:
    for seat in row:
        if seat == "#":
            result += 1
            
print(result)
