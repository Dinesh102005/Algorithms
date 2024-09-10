import heapq


def uniform_cost_search(graph, start, goal):
    # Priority queue to store nodes along with their cost
    priority_queue = []
    # Add the start node to the queue with a cost of 0
    heapq.heappush(priority_queue, (0, start))

    # To keep track of the visited nodes and their current minimum cost
    visited = {}
    visited[start] = 0

    # To keep track of the path
    parent = {}
    parent[start] = None

    while priority_queue:
        # Pop the node with the lowest cost
        current_cost, current_node = heapq.heappop(priority_queue)

        # If the goal is reached, return the cost and the path
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()  # Reverse the path to get the correct order
            return current_cost, path

        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            new_cost = current_cost + cost

            # If the neighbor is not visited or a lower cost path is found
            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor))
                parent[neighbor] = current_node

    return float('inf'), []  # Return if no path is found


# Example graph: (node -> [(neighbor, cost)])
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

start = 'A'
goal = 'F'
cost, path = uniform_cost_search(graph, start, goal)

print(f"Cost: {cost}, Path: {path}")
