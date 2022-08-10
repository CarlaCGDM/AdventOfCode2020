puzzle_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

numbers = puzzle_input.splitlines()

preamble = 5
current = preamble

for n in numbers[preamble:]:
    is_sum = False
    for i in numbers[current-preamble:current]:
        for j in numbers[current-preamble:current]:
            if i != j:
                if int(i)+int(j) == int(n):
                    is_sum = True
    if is_sum == False:
        print(n)
    current += 1
