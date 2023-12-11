import heapq, math
ROOT2 = math.sqrt(2)

inf = float('inf')


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
    26: {19: ROOT2, 25: 1, 31: ROOT2, 32: 1, 33: inf, 20:inf, 21:inf, 27:inf},
    27: {20:inf, 21:inf, 22:inf, 26:inf, 28:inf, 32:inf, 33:inf, 34:inf},
    28: {22: 1, 23: ROOT2, 29: 1, 33: inf, 34: 1, 35: ROOT2, 21:inf, 27:inf},
    29: {22: 1, 24: 1, 28: ROOT2, 29: 1, 30: ROOT2, 34: ROOT2, 35: 1, 36: ROOT2},
    30: {23: ROOT2, 24: 1, 29: 1, 35: ROOT2, 36: 1},
    31: {25: 1, 26: ROOT2, 32: 1},
    32: {25: ROOT2, 26: 1, 31: 1, 33: inf, 27:inf},
    33: {26: inf, 28: inf, 32: inf, 34: inf, 27:inf},
    34: {28: 1, 29: ROOT2, 33: inf, 35: 1, 27:inf},
    35: {28: ROOT2, 29: 1, 30: ROOT2, 34: 1, 36: 1},
    36: {29: ROOT2, 30: 1, 35: 1}  
}

class AStar:
    def __init__(self, graph):
        self.graph = graph

    def heuristic(self, node, goal):
        # Implement a heuristic function (Euclidean distance in this case)
        x1, y1 = node, node
        x2, y2 = goal, goal
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def astar(self, start, goal):
        open_set = []
        closed_set = set()

        heapq.heappush(open_set, (0, start, []))

        while open_set:
            current_cost, current_node, path = heapq.heappop(open_set)

            if current_node == goal:
                return path + [current_node]

            if current_node in closed_set:
                continue

            closed_set.add(current_node)

            for neighbor, cost in self.graph[current_node].items():
                if neighbor not in closed_set:
                    heuristic_cost = self.heuristic(neighbor, goal)
                    total_cost = current_cost + cost + heuristic_cost
                    heapq.heappush(open_set, (total_cost, neighbor, path + [current_node]))

        return None  # No path found

start_vertex = 5
end_vertex = 32  # Specify the ending vertex

astar = AStar(graph)
path = astar.astar(start_vertex, end_vertex)

if path:
    print("Path found:", path)
else:
    print("No path found.")
