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

def count_repeated_chars(group_answers):
    chars = list(group_answers[0])
    remove = []
    for line in group_answers:
        for char in chars:
            if char not in line:
                remove.append(char)
                
    for char in remove:
        if char in chars:
            chars.remove(char)
        
    return len(chars)
    
groups = []
group = []

for line in puzzle_input.splitlines():
    if line != "":
        group.append(line)
    else:
        groups.append(group)
        group = []
groups.append(group)
    
result = 0

for group in groups:
    result += count_repeated_chars(group)
    
print(result)
