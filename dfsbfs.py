graph = {
    'a' : [ 'b', 'g'],
    'b' : [ 'c' , 'f'],
    'c' : [ 'd' , 'e'],
    'd' : [] ,
    'e' : [],
    'f' : [],
    'g' : [ 'h'],
    'h' : ['i', 'j'],
    'i' : [],
    'j' :[]
}

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


visited = set()
dfs(graph, 'a', visited)

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


bfs(graph, 'a')
