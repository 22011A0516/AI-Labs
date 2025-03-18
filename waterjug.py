from collections import deque
import heapq

def dfs_water_jug(a, b, d):
  stack = [(0, 0)]
  visited = set([(0, 0)])
  while stack:
    jug_a, jug_b = stack.pop()
    print(f"Current state: ({jug_a}, {jug_b})")
    if jug_a == d or jug_b == d:
      return True
    possible_states = [
    ((a, jug_b), "Fill Jug A"),
    ((jug_a, b), "Fill Jug B"),
    ((0, jug_b),"Empty Jug A"),
    ((jug_a, 0), "Empty Jug B"),
    ((jug_a - min(jug_a, b - jug_b), jug_b + min(jug_a, b - jug_b)), "Pour Jug A into Jug B"),
    ((jug_a + min(jug_b, a - jug_a), jug_b - min(jug_b, a - jug_a)), "Pour Jug B into Jug A")
    ]
    for state, action in possible_states:
      if state not in visited:
        visited.add(state)
        stack.append(state)
        print(f"Action chosen: {action}, Next state: {state}")
  return False

def bfs_water_jug(a, b, d):
  queue = deque([(0, 0)])
  visited = set([(0, 0)])
  while queue:
    jug_a, jug_b = queue.popleft()
    print(f"Current state: ({jug_a}, {jug_b})")
    if jug_a == d or jug_b == d:
      return True
    possible_states = [
    ((a, jug_b), "Fill Jug A"),
    ((jug_a, b), "Fill Jug B"),
    ((0, jug_b), "Empty Jug A"),
    ((jug_a, 0), "Empty Jug B"),
    ((jug_a - min(jug_a, b - jug_b), jug_b + min(jug_a, b - jug_b)), "Pour Jug A into Jug B"),
    ((jug_a + min(jug_b, a - jug_a), jug_b - min(jug_b, a - jug_a)), "Pour Jug B into Jug A")
    ]
    for state, action in possible_states:
      if state not in visited:
        visited.add(state)
        queue.append(state)
        print(f"Action chosen: {action}, Next state: {state}")
return False

def ucs_water_jug(a, b, d):
  pq = []
  heapq.heappush(pq, (0, (0, 0)))
  visited = set([(0, 0)])
  while pq:
    cost, (jug_a, jug_b) = heapq.heappop(pq)
    print(f"Current state: ({jug_a}, {jug_b})")
    if jug_a == d or jug_b == d:
      return True
    possible_states = [
    ((a, jug_b), "Fill Jug A"),
    ((jug_a, b), "Fill Jug B"),
    ((0, jug_b), "Empty Jug A"),
    ((jug_a, 0), "Empty Jug B"),
    ((jug_a - min(jug_a, b - jug_b), jug_b + min(jug_a, b - jug_b)),"Pour Jug A into Jug B"),
    ((jug_a + min(jug_b, a - jug_a), jug_b - min(jug_b, a - jug_a)), "Pour Jug B into Jug A")
    ]
    for state, action in possible_states:
      if state not in visited:
        visited.add(state)
        heapq.heappush(pq, (cost + 1, state))
        print(f"Action chosen: {action}, Next state: {state}")
  return False
a = 4
b = 3
d = 2

print("DFS:")
if dfs_water_jug(a, b, d):
  print("Solution found!")
else:
  print("No solution.")
  
print("\nBFS:")
if bfs_water_jug(a, b, d):
  print("Solution found!")
else:
  print("No solution.")

print("\nUCS:")
if ucs_water_jug(a, b, d):
  print("Solution found!")
else:
  print("No solution.")
