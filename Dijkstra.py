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
    
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]
    # Dictionary to store distances from the start vertex
    distances = {vertex: float('infinity') for vertex in range(1, 37)}
    distances[start] = 0

    visited = set()
  
    while priority_queue:
            # Get the vertex with the smallest distance
            current_distance, current_vertex = heapq.heappop(priority_queue)
            coords = [(current_vertex - 1) // 6, (current_vertex - 1) % 6]

            # Check if the current path is longer than the known distance
            if current_vertex in visited:
                continue
            
            # Mark the current vertex as visited
            visited.add(current_vertex)
            
            front = []
            # Update distances for neighboring vertices
            for d in directions:
                if coords[0] + d[0] < 6 and coords[0] + d[0] >= 0 and coords[1] + d[1] < 6 and coords[1] + d[1] >= 0:
                    weight = 0
                    if d[0] == 0 or d[1] == 0:
                        weight = 1
                    else:
                        weight = ROOT2
                    neighbour = graph[coords[0] + d[0]][coords[1] + d[1]]
                    if neighbour == -1:
                        continue
                    distance = current_distance + weight
                    
                    front.append([weight, neighbour, current_vertex])
                    # If a shorter path is found, update the distance
                    if distance < distances[neighbour]:
                        distances[neighbour] = distance
                        heapq.heappush(priority_queue, (distance, neighbour))
            
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
    print(distances)
    path = []
    current_vertex = end
    while current_vertex != start:
        path.insert(0, current_vertex)
        coords = [(current_vertex - 1) // 6, (current_vertex - 1) % 6]
        for d in directions:
            if coords[0] + d[0] < 6 and coords[0] + d[0] >= 0 and coords[1] + d[1] < 6 and coords[1] + d[1] >= 0:
                v = graph[coords[0] + d[0]][coords[1] + d[1]]
                if v == -1:
                    continue
                if distances[v] < distances[current_vertex]:
                    current_vertex = v

    path.insert(0, start)

    return distances[end], path


# Initialize the grid with obstacles
graph = [
    [1,   -1,    3,     4,     5,     6],
    [7,    8,    9,    -1,    -1,    12],
    [13,  14,   15,    16,    17,    18],
    [19,  -1,   -1,    22,    23,    24],
    [25,  26,   -1,    28,    29,    30],
    [31,  32,   33,    34,    35,    36]
]

start_vertex = 5
end_vertex = 32  # Specify the ending vertex

result, path = dijkstra(graph, start_vertex, end_vertex)


print(f"Shortest distance from {start_vertex} to {end_vertex}: {result} \nWith the path: {path}")