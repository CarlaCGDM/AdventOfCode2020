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
adapters.append(0)

adapters.sort()

#figure out which adapters can connect to the current joltage

def find_connections(current_adapter,adapters):
    connections = []
    for adapter in adapters:
        if (adapter - current_adapter) in range(1,4):
            connections.append(adapter)
    return connections
  
#build graph

connections = {}

for adapter in adapters:
    connections[adapter] = find_connections(adapter,adapters)
    
 #find paths

def find_all_paths(graph,start,end,path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        new_paths = find_all_paths(graph, node, end, path)
        for new_path in new_paths:
            paths.append(new_path)
    return paths
        
print(len(find_all_paths(connections,0,my_adapter)))
    
