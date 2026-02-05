#to implement A* search

graph = {
    'S' :{'A' : 5 , 'B' : 9 , 'D' : 6},
    'A': { 'B': 3 , 'G1' :0 },
    'D' : {'E' : 2 ,'C' : 2 , },
    'B' : { 'C': 1 , 'A' : 2},
    'C' : { 'G2': 5 , 'F' : 6 ,'S' : 6 }, #write time complexity and space complexity
    'E' : { 'G3': 7 },
    'F' : { 'D' : 2, 'G3' : 8},
    'G1':{} , 'G2': {} , 'G3' : {}


}

heuristic = {
    'S' : 5 ,'A' : 7, 'B' :3 , 'C': 4, 'D': 2, 'E' : 5, 'F' : 5, 'G1': 0,
    'G2': 0 , 'G3': 0
}



import heapq

def a_star(start, goals, graph, heuristic):
    open_list = []                     # priority queue
    closed_list = set()                # empty set

    g = {start: 0}
    f = {start: heuristic[start]}
    parent = {start: None}

    heapq.heappush(open_list, (f[start], start))

    while open_list:
        _, current = heapq.heappop(open_list)

        if current in goals:
            return reconstruct_path(parent, current)

        closed_list.add(current)

        for neighbor, cost in graph[current].items():
            temp_g = g[current] + cost

            if neighbor in closed_list and temp_g >= g.get(neighbor, float('inf')):
                continue

            if neighbor not in g or temp_g < g[neighbor]:
                parent[neighbor] = current
                g[neighbor] = temp_g
                f[neighbor] = g[neighbor] + heuristic[neighbor]

                heapq.heappush(open_list, (f[neighbor], neighbor))

    return "FAIL"

def reconstruct_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]

path = a_star('S', {'G1', 'G2', 'G3'}, graph, heuristic)
print("Path found:", path)

path = a_star('S', {'G1', 'G2', 'G3'}, graph, heuristic)
print("Path found:", path)

def reconstruct_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


path, cost = a_star('S', {'G1', 'G2', 'G3'}, graph, heuristic)

print("Shortest path:", path)
print("Total cost:", cost)
