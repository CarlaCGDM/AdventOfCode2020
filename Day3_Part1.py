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
    
width = len(tree_map[0])-1

#if index is too big we subtract the width to loop over

col = 3
trees = 0

for row in tree_map:
    if col > width:
        col -= width
    if row[col] == '#':
        trees += 1
    col += 3

print(trees)
