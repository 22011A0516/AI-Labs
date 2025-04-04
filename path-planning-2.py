import heapq
rows, cols = 4, 6
goal = (3, 5)
walls = {
((2, 2), (2, 3)),
((3, 2), (3, 3)),
((4, 2), (4,3)),
((1, 5), (2, 5)),
((1, 6), (2, 6)),
}
directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

def manhattan_heuristic(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])
  
def chebyshev_heuristic(a, b):
  return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def is_move_valid(curr, neighbor):
  if (curr, neighbor) in walls or (neighbor, curr) in walls:
    return False
  return True
  
def a_star(start, goal, heuristic_func):
  open_list = []
  heapq.heappush(open_list, (0 + heuristic_func(start, goal), 0, start))
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
        f_cost = next_cost + heuristic_func(next_node, goal)
        heapq.heappush(open_list, (f_cost, next_cost, next_node))
        parent[next_node] = current_node
  return -1, []

def convert_to_letter(col):
  return chr(ord('A') + col - 1)

r = int(input("Enter starting row no:"))
c = int(input("Enter starting column no:"))
start = (r, c)
manhattan_cost, manhattan_path = a_star(start, goal, manhattan_heuristic)
chebyshev_cost, chebyshev_path = a_star(start, goal, chebyshev_heuristic)

if manhattan_cost != -1:
  print(f"Manhattan Path Cost from {start} to goal {goal}: {manhattan_cost}")
  print("Manhattan Path Taken:", "->".join([f"({x}, {convert_to_letter(y)})" for x, y in
  manhattan_path]))
else:
  print("No path found using Manhattan distance!")
if chebyshev_cost != -1:
  print(f"Chebyshev Path Cost from {start} to goal {goal}: {chebyshev_cost}")
  print("Chebyshev Path Taken:", "->".join([f&quot;({x}, {convert_to_letter(y)})" for x, y in
  chebyshev_path]))
else:
  print("No path found using Chebyshev distance!")
