import heapq, math

ROOT2 = math.sqrt(2)
inf = float('inf')

open("astar_front.txt", "w").close()
open("astar_visited.txt", "w").close()

front_file = open("astar_front.txt", "a")
visited_file = open("astar_visited.txt", "a")

def heuristic(a, b):
    # A simple heuristic function (Euclidean distance)
    x1, y1 = (a - 1) // 6, (a - 1) % 6
    x2, y2 = (b - 1) // 6, (b - 1) % 6
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def astar(graph, start, end, obstacles):
    priority_queue = [(0 + heuristic(start, end), 0, start)]
    iterations = 0

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]
    distances = {vertex: float('infinity') for vertex in range(1, 37)}
    distances[start] = 0

    visited = set()

    while priority_queue:
        current_total_cost, current_distance, current_vertex = heapq.heappop(priority_queue)
        coords = [(current_vertex - 1) // 6, (current_vertex - 1) % 6]

        if current_vertex in visited or current_vertex in obstacles:
            continue

        visited.add(current_vertex)

        front = []
        for d in directions:
            if coords[0] + d[0] < 6 and coords[0] + d[0] >= 0 and coords[1] + d[1] < 6 and coords[1] + d[1] >= 0:
                weight = 0
                if d[0] == 0 or d[1] == 0:
                    weight = 1
                else:
                    weight = ROOT2
                neighbour = graph[coords[0] + d[0]][coords[1] + d[1]]
                if neighbour == -1 or neighbour in obstacles:
                    continue
                distance = current_distance + weight
                total_cost = distance + heuristic(neighbour, end)

                front.append([weight, neighbour, current_vertex])
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    heapq.heappush(priority_queue, (total_cost, distance, neighbour))

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

    print(distances)
    path = []
    current_vertex = end
    while current_vertex != start:
        path.insert(0, current_vertex)
        coords = [(current_vertex - 1) // 6, (current_vertex - 1) % 6]
        for d in directions:
            if coords[0] + d[0] < 6 and coords[0] + d[0] >= 0 and coords[1] + d[1] < 6 and coords[1] + d[1] >= 0:
                v = graph[coords[0] + d[0]][coords[1] + d[1]]
                if v == -1 or v in obstacles:
                    continue
                if distances[v] < distances[current_vertex]:
                    current_vertex = v

    path.insert(0, start)

    return distances[end], path

# Initialize the graph with obstacles
graph = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]

obstacles = [2, 10, 11, 20, 21, 27, 33]

start_vertex = 16
end_vertex = 32

result, path = astar(graph, start_vertex, end_vertex, obstacles)

print(f"Shortest distance from {start_vertex} to {end_vertex}: {result} \nWith the path: {path}")
