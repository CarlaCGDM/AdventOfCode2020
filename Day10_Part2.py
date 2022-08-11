puzzle_input = """16
10
15
5
1
11
7
19
6
12
4"""

adapters = puzzle_input.splitlines()
adapters = [int(x) for x in adapters]

my_adapter = max(adapters) + 3
adapters.append(my_adapter)

adapters.sort()

#count adapters

tally = {0 : 1}

for adapter in adapters:
    tally[adapter] = tally.get(adapter-3,0) + tally.get(adapter-2,0) + tally.get(adapter-1,0)

print(tally[adapters[-1]])
