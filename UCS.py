import heapq
infinity = 1111
graph = {
'S':[('p',1),('d',3),('e',9)],
'r': [('f', 1)],
'a': [],
'e': [('h', 8), ('r', 2)],
'd': [('c', 8), ('e', 2), ('b', 1)],
&#39;p&#39;: [(&#39;q&#39;, 15)],
&#39;b&#39;: [(&#39;a&#39;, 2)],
&#39;f&#39;: [(&#39;G&#39;, 2), (&#39;c&#39;, infinity)],
&#39;q&#39;: [],
&#39;h&#39;: [(&#39;p&#39;, infinity), (&#39;q&#39;, infinity)],
&#39;c&#39;: [(&#39;a&#39;, infinity)],
&#39;G&#39;: []
}
start_node = 'S';
end_node = 'G';
hp = []
heapq.heappush(hp, (0, start_node))

visited_nodes = set()
node_costs = {start_node: 0}

while hp:
  current_cost, current_node = heapq.heappop(hp)
  if current_node in visited_nodes:
    continue
  visited_nodes.add(current_node)
  print(f&quot;Visiting: {current_node} (Cost: {current_cost})&quot;)
  if current_node == end_node:
    print(f"Reached {end_node} with cost {current_cost}")
    break
  for neighbor, weight in graph.get(current_node, []):
    new_cost = current_cost + weight
    if neighbor not in visited_nodes or new_cost &lt; node_costs.get(neighbor,infinity):
      heapq.heappush(hp, (new_cost, neighbor))
      node_costs[neighbor] = new_cost
      print(f"Queueing {neighbor} (Cost: {new_cost})")
    else:
      print(f"Cost from {start_node} to {end_node}: {infinity}")
