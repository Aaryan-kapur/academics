nodes = ('0', '1', '2', '3', '4', '5', '6','7','8')
distances = {
    '0': {'1': 4, '7': 8},
    '1': {'0': 4, '2': 8, '7': 11},
    '2': {'1': 8, '3': 7, '5': 4, '8': 2},
    '3': {'2': 7, '4': 9, '5': 14},
    '4': {'3': 9, '5': 10},
    '5': {'2': 4, '3': 14, '4': 10, '6' : 2},
    '6': {'5': 2, '7': 1, '8': 6},
    '7': {'0': 8, '1': 11, '6': 1 , '8' :7},
    '8': {'2': 2, '6': 6, '7': 7}
    }

unvisited = {node: None for node in nodes} 
visited = {}
source = '0'
terminal = '4'
sourceDistance = 0
unvisited[source] = sourceDistance

while True:
    for neighbour, distance in distances[source].items():
        if neighbour not in unvisited: continue
        newDistance = sourceDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[source] = sourceDistance
    del unvisited[source]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    source, sourceDistance = sorted(candidates, key = lambda x: x[1])[0]
print(visited[terminal])
