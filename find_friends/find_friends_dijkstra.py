def find_friends(u1, u2, friends, max_depth):
  """ 
  A Dijkstra-like BFS approach that keeps track of distance to a node
  and the previous node in the shortest path to it
  """

  # Keep track of known nodes, their distance score, and prev-nodes
  nodes = {u1: (1, None)}
  nodes_to_check = [u1]

  def rebuild_path_to(node):
    """ Recursively re-build the path to a node """
    distance, prev_node = nodes[node]
    if prev_node == None:
      return [node]
    else:
      return rebuild_path_to(prev_node) + [node]
    
  while nodes_to_check:
    curr_node = nodes_to_check.pop()
    curr_distance, prev_node = nodes[curr_node]
    if curr_node == u2:
      return rebuild_path_to(curr_node)
    elif curr_distance < max_depth:
      for f in friends[curr_node]:
        if f in nodes:
          # We dont want to over-write a better path
          distance, prev_node = nodes[f]
          if distance <= curr_distance + 1:
            continue
        nodes[f] = (curr_distance +1, curr_node)
        nodes_to_check.append(f)
  return []
      
    
  


