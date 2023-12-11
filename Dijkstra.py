import heapq, math
ROOT2 = math.sqrt(2)

def dijkstra(graph, start, end):
    # Priority queue to store vertices and their distances
    priority_queue = [(0, start)]
    
    # Dictionary to store distances from the start vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    while priority_queue:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Check if the current path is longer than the known distance
        if current_distance > distances[current_vertex]:
            continue
        
        # Update distances for neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # If a shorter path is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances[end]

# Example usage:
graph = {
    1: {7: 1, 8: ROOT2},
    3: {8: ROOT2, 9: ROOT2, 4: 1},
    4: {9: ROOT2, 5: 1},
    5: {4: 1, 6: 1, 12: ROOT2},
    6: {12: 1, 5: 1},
    7: {1: 1, 8: 1, 14: ROOT2, 13: 1},
    8: {1: ROOT2, 7: 1, 13: ROOT2, 14: 1, 15: ROOT2, 9: 1, 3: ROOT2},
    9: {3: 1, 15: 1, 8: 1, 4: ROOT2, 14: ROOT2, 16: ROOT2},
    12: {6: 1, 18: 1, 5: ROOT2, 17: ROOT2},
    13: {7: 1, 14: 1, 19: 1, 8: ROOT2},
    14: {8: 1, 9: ROOT2, 15: 1, 13: 1, 7: ROOT2, 19: ROOT2},
    15: {9: 1, 14: 1, 16: 1, 22: ROOT2, 8: ROOT2},
    16: {22: 1, 15: 1, 17: 1, 9: ROOT2, 23: ROOT2},
    17: {23: 1, 18: 1, 16: 1, 22: ROOT2, 24: ROOT2},
    18: {12: 1, 24: 1, 17: 1, 23: ROOT2},
    19: {13: 1, 14: ROOT2, 25: 1, 26: ROOT2},
    22: {15: ROOT2, 16: 1, 17: ROOT2, 23: 1, 28: 1, 29: ROOT2},
    23: {16: ROOT2, 17: 1, 18: ROOT2, 22: 1, 24: 1, 28: ROOT2, 29: 1, 30: ROOT2},
    24: {17: ROOT2, 18: 1, 23: 1, 29: ROOT2, 30: 1},
    25: {19: 1, 26: 1, 31: 1, 32: ROOT2},
    26: {19: ROOT2, 25: 1, 31: ROOT2, 32: 1, 33: ROOT2},
    28: {22: 1, 23: ROOT2, 29: 1, 33: ROOT2, 34: 1, 35: ROOT2},
    29: {22: 1, 24: 1, 28: ROOT2, 29: 1, 30: ROOT2, 34: ROOT2, 35: 1, 36: ROOT2},
    30: {23: ROOT2, 24: 1, 29: 1, 35: ROOT2, 36: 1},
    31: {25: 1, 26: ROOT2, 32: 1},
    32: {25: ROOT2, 26: 1, 31: 1, 33: 1},
    33: {26: ROOT2, 28: ROOT2, 32: 1, 34: 1},
    34: {28: 1, 29: ROOT2, 33: 1, 35: 1},
    35: {28: ROOT2, 29: 1, 30: ROOT2, 34: 1, 36: 1},
    36: {29: ROOT2, 30: 1, 35: 1}
    
}

start_vertex = 5
end_vertex = 32  # Specify the ending vertex
result = dijkstra(graph, start_vertex, end_vertex)

print(f"Shortest distance from {start_vertex} to {end_vertex}: {result}")