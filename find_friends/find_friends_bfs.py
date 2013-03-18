def find_friends(u1, u2, friends, max_depth):
  """
  Using BFS and keeping paths as nodes
  """
  paths_to_check = [[u1]]
  while paths_to_check:
    curr_path = paths_to_check.pop()
    curr_node = curr_path[-1]
    if curr_node == u2:
      return curr_path
    elif len(curr_path) < max_depth:
      for friend in friends[curr_node]:
        paths_to_check.append(curr_path + [friend])
  return []

def find_friends2(u1, u2, friends, max_depth):
  """
  Using BFS and keeping paths in a global dict
  """
  nodes_to_visit = [u1]
  paths_to_node = {u1: []}
  while nodes_to_visit:
    curr_node = nodes_to_visit.pop()
    curr_path = paths_to_node[curr_node] + [curr_node]
    if curr_node == u2:
      return curr_path
    elif len(curr_path) < max_depth:
      for friend in friends[curr_node]:
          paths_to_node[friend] = curr_path
          nodes_to_visit.append(friend)
  return []
      
