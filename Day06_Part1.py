puzzle_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""

#Answers by the same person are in the same line
#Answers by different groups are separated by empty lines

def count_unique_chars(group_answers):
    chars = set()
    for ch in group_answers:
        if ch != "\n":
            chars.add(ch)
    return len(chars)
    
groups = []

group = ""
for line in puzzle_input.splitlines():
    if line != "":
        group+=line
    else:
        groups.append(group)
        group = ""
groups.append(group)
    
result = 0

for group in groups:
    result += count_unique_chars(group)
    
print(result)
