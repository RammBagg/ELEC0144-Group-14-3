import heapq, math
ROOT2 = math.sqrt(2)

inf = float('inf')

open("dijkstra_front.txt", "w").close()
open("dijkstra_visited.txt", "w").close()

front_file = open("dijkstra_front.txt", "a")
visited_file = open("dijkstra_visited.txt", "a")

def dijkstra(graph, start, end):
    # Priority queue to store vertices and their distances
    priority_queue = [(0, start)]
    iterations = 0
    
    # Dictionary to store distances from the start vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    visited = set()
  
    while priority_queue:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Check if the current path is longer than the known distance
        if current_vertex in visited:
            continue
        
        # Mark the current vertex as visited
        visited.add(current_vertex)
        
        front = []
        # Update distances for neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            front.append([weight, neighbor, current_vertex])
            # If a shorter path is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
        
        visited_file.write(f"Iteration {iterations}: ")
        visited_file.write(str(visited) + "\n")

        front_file.write(f"Iteration {iterations}: \n")
        write_to_file = "{ \n"
        for s in front:
            write_to_file += str(s) + "\n"
        write_to_file += "} \n\n"

        front_file.write(write_to_file)

        iterations += 1

    visited_file.close()
    front_file.close()

    # Backpropagation to find the shortest path
    path = []
    current_vertex = end
    while current_vertex != start:
        path.insert(0, current_vertex)
        current_vertex = min(graph[current_vertex], key=lambda x: distances[x])

    path.insert(0, start)

    return distances[end], path

# Example usage:
graph = {
    1: {7: 1, 2:inf, 8: ROOT2},
    2: {1: inf, 7:inf, 8:inf, 9:inf, 3:inf},
    3: {2:inf, 8: ROOT2, 9: ROOT2, 4: 1},
    4: {10:inf, 11:inf, 9: ROOT2, 5: 1, 3: 1},
    5: {11:inf, 10:inf, 4: 1, 6: 1, 12: ROOT2},
    6: {12: 1, 5: 1, 11:inf},
    7: {1: 1, 8: 1, 14: ROOT2, 13: 1},
    8: {2:inf, 1: ROOT2, 7: 1, 13: ROOT2, 14: 1, 15: ROOT2, 9: 1, 3: ROOT2},
    9: {2:inf, 3: 1, 15: 1, 8: 1, 4: ROOT2, 14: ROOT2, 16: ROOT2, 10:inf},
    10: {3:inf, 4:inf, 5:inf, 11:inf, 17:inf, 16:inf, 15:inf, 9:inf},
    11: {5:inf, 6:inf, 12:inf, 18:inf, 17:inf, 16:inf, 10:inf, 4:inf},
    12: {11:inf, 6: 1, 18: 1, 5: ROOT2, 17: ROOT2},
    13: {20:inf, 7: 1, 14: 1, 19: 1, 8: ROOT2},
    14: {20:inf, 8: 1, 9: ROOT2, 15: 1, 13: 1, 7: ROOT2, 19: ROOT2, 21:inf},
    15: {9: 1, 14: 1, 16: 1, 22: ROOT2, 8: ROOT2, 20:inf, 21:inf, 10:inf},
    16: {22: 1, 15: 1, 17: 1, 9: ROOT2, 23: ROOT2},
    17: {23: 1, 18: 1, 16: 1, 22: ROOT2, 24: ROOT2},
    18: {11:inf, 12: 1, 24: 1, 17: 1, 23: ROOT2},
    19: {20:inf, 13: 1, 14: ROOT2, 25: 1, 26: ROOT2},
    20: {14:inf, 13:inf, 19:inf, 25:inf, 26:inf, 27:inf, 21:inf, 15:inf, 14:inf},
    21: {14: inf, 15: inf, 16:inf, 22: inf, 27: inf, 28: inf, 20:inf, 26:inf},
    22: {15: ROOT2, 16: 1, 17: ROOT2, 23: 1, 28: 1, 29: ROOT2, 21:inf, 27:inf},
    23: {16: ROOT2, 17: 1, 18: ROOT2, 22: 1, 24: 1, 28: ROOT2, 29: 1, 30: ROOT2},
    24: {17: ROOT2, 18: 1, 23: 1, 29: ROOT2, 30: 1},
    25: {19: 1, 26: 1, 31: 1, 32: ROOT2, 20:inf},
    26: {19: ROOT2, 25: 1, 31: ROOT2, 32: 1, 33: ROOT2, 20:inf, 21:inf, 27:inf},
    27: {20:inf, 21:inf, 22:inf, 26:inf, 28:inf, 32:inf, 33:inf, 34:inf},
    28: {22: 1, 23: ROOT2, 29: 1, 33: ROOT2, 34: 1, 35: ROOT2, 21:inf, 27:inf},
    29: {22: 1, 24: 1, 28: ROOT2, 29: 1, 30: ROOT2, 34: ROOT2, 35: 1, 36: ROOT2},
    30: {23: ROOT2, 24: 1, 29: 1, 35: ROOT2, 36: 1},
    31: {25: 1, 26: ROOT2, 32: 1},
    32: {25: ROOT2, 26: 1, 31: 1, 33: 1, 27:inf},
    33: {26: ROOT2, 28: ROOT2, 32: 1, 34: 1, 27:inf},
    34: {28: 1, 29: ROOT2, 33: 1, 35: 1, 27:inf},
    35: {28: ROOT2, 29: 1, 30: ROOT2, 34: 1, 36: 1},
    36: {29: ROOT2, 30: 1, 35: 1}  
}

start_vertex = 5
end_vertex = 32  # Specify the ending vertex
result, path = dijkstra(graph, start_vertex, end_vertex)

print(f"Shortest distance from {start_vertex} to {end_vertex}: {result} \nWith the path: {path}")