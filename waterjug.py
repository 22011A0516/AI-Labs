from collections import deque
import heapq

def dfs_water_jug(a, b, d):
  stack = [(0, 0)]
  visited = set([(0, 0)])
  while stack:
    jug_a, jug_b = stack.pop()
    print(f&quot;Current state: ({jug_a}, {jug_b})&quot;)
    if jug_a == d or jug_b == d:
      return True
    possible_states = [
    ((a, jug_b), &quot;Fill Jug A&quot;),
    ((jug_a, b), &quot;Fill Jug B&quot;),
    ((0, jug_b), &quot;Empty Jug A&quot;),
    ((jug_a, 0), &quot;Empty Jug B&quot;),
    ((jug_a - min(jug_a, b - jug_b), jug_b + min(jug_a, b - jug_b)), &quot;Pour Jug A into Jug B&quot;),
    ((jug_a + min(jug_b, a - jug_a), jug_b - min(jug_b, a - jug_a)), &quot;Pour Jug B into Jug A&quot;)
    ]
    for state, action in possible_states:
      if state not in visited:
        visited.add(state)
        stack.append(state)
        print(f&quot;Action chosen: {action}, Next state: {state}&quot;)
  return False

def bfs_water_jug(a, b, d):
  queue = deque([(0, 0)])
  visited = set([(0, 0)])
  while queue:
    jug_a, jug_b = queue.popleft()
    print(f&quot;Current state: ({jug_a}, {jug_b})&quot;)
    if jug_a == d or jug_b == d:
      return True
    possible_states = [
    ((a, jug_b), &quot;Fill Jug A&quot;),
    ((jug_a, b), &quot;Fill Jug B&quot;),
    ((0, jug_b), &quot;Empty Jug A&quot;),
    ((jug_a, 0), &quot;Empty Jug B&quot;),
    ((jug_a - min(jug_a, b - jug_b), jug_b + min(jug_a, b - jug_b)), &quot;Pour Jug A into Jug B&quot;),
    ((jug_a + min(jug_b, a - jug_a), jug_b - min(jug_b, a - jug_a)), &quot;Pour Jug B into Jug A&quot;)
    ]
    for state, action in possible_states:
      if state not in visited:
        visited.add(state)
        queue.append(state)
        print(f&quot;Action chosen: {action}, Next state: {state}&quot;)
return False

def ucs_water_jug(a, b, d):
pq = []
heapq.heappush(pq, (0, (0, 0)))
visited = set([(0, 0)])
while pq:
  cost, (jug_a, jug_b) = heapq.heappop(pq)
  print(f&quot;Current state: ({jug_a}, {jug_b})&quot;)
  if jug_a == d or jug_b == d:
    return True
  possible_states = [
  ((a, jug_b), &quot;Fill Jug A&quot;),
  ((jug_a, b), &quot;Fill Jug B&quot;),
  ((0, jug_b), &quot;Empty Jug A&quot;),
  ((jug_a, 0), &quot;Empty Jug B&quot;),
  ((jug_a - min(jug_a, b - jug_b), jug_b + min(jug_a, b - jug_b)), &quot;Pour Jug A into Jug B&quot;),
  ((jug_a + min(jug_b, a - jug_a), jug_b - min(jug_b, a - jug_a)), &quot;Pour Jug B into Jug A&quot;)
  ]
  for state, action in possible_states:
    if state not in visited:
      visited.add(state)
      heapq.heappush(pq, (cost + 1, state))
      print(f&quot;Action chosen: {action}, Next state: {state}&quot;)
return False
a = 4
b = 3
d = 2

print(&quot;DFS:&quot;)
if dfs_water_jug(a, b, d):
  print(&quot;Solution found!&quot;)
else:
  print(&quot;No solution.&quot;)
  
print(&quot;\nBFS:&quot;)
if bfs_water_jug(a, b, d):
  print(&quot;Solution found!&quot;)
else:
  print(&quot;No solution.&quot;)

print(&quot;\nUCS:&quot;)
if ucs_water_jug(a, b, d):
  print(&quot;Solution found!&quot;)
else:
  print(&quot;No solution.&quot;)
