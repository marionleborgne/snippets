def find_friends(u1, u2, friends, max_depth):
  """
  Using bounded DFS with recursion
  """

  best_path = None
  if max_depth == 0:
    return []
  elif u1 == u2:
    return [u1]
  else:
    for f in friends[u1]:
      path = find_friends(f, u2, friends, max_depth-1)
      if path and (not best_path or len(best_path) > len(path)):
        best_path = path
    if best_path:
      return [u1] + best_path
    else:
      return []
