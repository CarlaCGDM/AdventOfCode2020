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
result = 0

for n in numbers[preamble:]:
    is_sum = False
    for i in numbers[current-preamble:current]:
        for j in numbers[current-preamble:current]:
            if i != j:
                if int(i)+int(j) == int(n):
                    is_sum = True
    if is_sum == False:
        result = int(n)
        break
    current += 1
    
for i in range(0,len(numbers)-1):
    #keep adding while sum is smaller than result
    total_sum = 0
    numbers_in_range = []
    current = 0
    while total_sum < result:
        total_sum += int(numbers[i+current])
        numbers_in_range.append(int(numbers[i+current]))
        current += 1
    if total_sum == result:
        print(min(numbers_in_range)+max(numbers_in_range))
        break
