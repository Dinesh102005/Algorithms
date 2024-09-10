#dls
def depth_limited_search(graph, start, goal, depth_limit):
    if start == goal:
        return [start]

    if depth_limit == 0:
        return None

    if start not in graph:
        return None

    for neighbor in graph[start]:
        result = depth_limited_search(graph, neighbor, goal, depth_limit - 1)
        if result is not None:
            return [start] + result

    return None

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['K'],
    'D': ['J','K'],
    'E': [],
    'F': ['G'],
    'G': ['H'],
    'H': ['I'],
    'I': []
}

start_node = 'A'
goal_node = 'K'
depth_limit = 4

path = depth_limited_search(graph, start_node, goal_node, depth_limit)

if path is not None:
    print("Path found:", path)
else:
    print("Path not found within depth limit.")