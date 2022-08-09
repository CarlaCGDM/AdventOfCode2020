puzzle_input = """FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""

#Rows: ranging from 0 to 127, on each letter you split the range in half and keep the upper ("F") or lower ("B") half.

#Columns: ranging from 0 to 7, on each letter you split the range in half and keep the upper ("L") or lower ("R") half.

#Every seat also has a unique seat ID: multiply the row by 8, then add the column.


def row_and_column(boarding_pass:str):
    row = [0,127]
    col = [0,7]
    
    for letter in boarding_pass[:7]:
        if letter == "F":
            row[1] = row[0] + (row[1]-row[0])//2
        if letter == "B":
            row[0] = row[0] + (row[1]-row[0])//2 + 1
        
    for letter in boarding_pass[7:]:
        if letter == "L":
            col[1] = col[0] + (col[1]-col[0])//2
        if letter == "R":
            col[0] = col[0] + (col[1]-col[0])//2 + 1

    seat_id = row[0]*8 + col[0]
    return seat_id

boarding_passes = []

for boarding_pass in puzzle_input.splitlines():
    boarding_passes.append(row_and_column(boarding_pass))
    
print(max(boarding_passes))
