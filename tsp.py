import itertools
import random
dist = {
  (1, 2): 20, (1, 3): 10, (1, 4): 15,
  (2, 1): 20, (2, 3): 15, (2, 4): 11,
  (3, 1): 10, (3, 2): 15, (3, 4): 17,
  (4, 1): 15, (4, 2): 11, (4, 3): 17
}
def total_distance(tour):
  dist_sum = 0
  for i in range(len(tour) - 1):
    dist_sum += dist.get((tour[i], tour[i+1]), dist.get((tour[i+1], tour[i])))
  dist_sum += dist.get((tour[-1], tour[0]), dist.get((tour[0], tour[-1]))) # returning to the origin
  return dist_sum
  
def two_opt(tour):
  neighbors = []
  for i, j in itertools.combinations(range(len(tour)), 2):
    if i &lt; j:
      new_tour = tour[:i] + list(reversed(tour[i:j+1])) + tour[j+1:]
      neighbors.append(new_tour)
  return neighbors

def hill_climbing(tour):
  current_tour = tour
  current_distance = total_distance(current_tour)
  while True:
    neighbors = two_opt(current_tour)
    best_neighbor = None
    best_distance = current_distance
    for neighbor in neighbors:
      dist = total_distance(neighbor)
      if dist &lt; best_distance:
        best_distance = dist
        best_neighbor = neighbor
    if best_neighbor is None:
      break
    else:
      current_tour = best_neighbor
      current_distance = best_distance
  return current_tour, current_distance

cities = [1, 2, 3, 4]
random_start_states = [random.sample(cities, len(cities)) for _ in range(3)]

for i, start_state in enumerate(random_start_states):
  best_tour, best_distance = hill_climbing(start_state)
  print(f&quot;Random start {i+1}: {start_state}&quot;)
  print(f&quot;Best tour: {best_tour}&quot;)
  print(f&quot;Best distance: {best_distance}&quot;)
  print(&quot;-&quot; * 40)
