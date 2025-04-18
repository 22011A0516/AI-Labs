import heapq
rows, cols = 4, 6
goal = (3, 6)
walls = {
    ((2, 2), (2, 3)),
    ((3, 2), (3, 3)),
    ((4, 2), (4, 3)),
    ((2, 5), (3, 5)),
    ((2, 6), (3, 6)),
}
directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_move_valid(curr, neighbor):
    if (curr, neighbor) in walls or (neighbor, curr) in walls:
        return False
    return True

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))
    visited = set()
    g_cost = {start: 0}
    parent = {start: None}
    
    while open_list:
        _, current_cost, current_node = heapq.heappop(open_list)
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return current_cost, path
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for dx, dy in directions:
            next_node = (current_node[0] + dx, current_node[1] + dy)
            if not (1 <= next_node[0] <= rows and 1 <= next_node[1] <= cols):
                continue
            if not is_move_valid(current_node, next_node):
                continue
            next_cost = current_cost + 1
            if next_node not in g_cost or next_cost < g_cost[next_node]:
                g_cost[next_node] = next_cost
                f_cost = next_cost + heuristic(next_node, goal)
                heapq.heappush(open_list, (f_cost, next_cost, next_node))
                parent[next_node] = current_node
    return -1, []
row_input = int(input("Enter row (1-4): "))
col_input = input("Enter column (A-F): ").upper()

start = (row_input, ord(col_input) - ord('A') + 1)
cost, path = a_star(start, goal)

if cost != -1:
    print(f"Optimal path cost from {start} to goal {goal}: {cost}")
    print("Path taken:", " -> ".join([f"({x}, {chr(y + ord('A') - 1)})" for x, y in path]))
else:
    print("No path found to the goal!")

