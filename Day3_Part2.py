
puzzle_input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

tree_map = []

rows = puzzle_input.splitlines()
for r in rows:
    tree_map.append(list(r))
    
width = len(tree_map[0])

#if index is too big we subtract the width to loop over

def trees_on_path(right,down):
    trees = 0
    row_num = 1
    col = right
    
    for row in tree_map[1:]:
        if row_num%down == 0:
            if row[col] == '#':
                trees += 1
            col += right
            if col >= width:
                col -= width
        row_num += 1
    return trees

path1 = trees_on_path(1,1)
path2 = trees_on_path(3,1)
path3 = trees_on_path(5,1)
path4 = trees_on_path(7,1)
path5 = trees_on_path(1,2)

print(path1*path2*path3*path4*path5)
