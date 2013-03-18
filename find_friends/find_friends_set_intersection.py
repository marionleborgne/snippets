"""
A BFS-like approach but using the start and end node simoultaneously.

Intuition: 
  If A and B have a friend in common ( A->F->B ), then the set intersection of
  their friend-sets will contain F. If a mutual friend isn't found, expand the
  "frontier" of A's friends to consist of friends-of-friends. Still no luck?
  Expand B's frontier.

  To reconstruct the final path A->..->B, keep track of paths to each node in
  each frontier.
  
  Complicated, but does about 1/2 the work of regular BFS.

"""

class Frontier(object):
  def __init__(self, start_node):
    self.nodes = set([start_node])
    self.paths = {start_node: []}

  def __and__(self, other):
    # Frontiers are really just sets..
    return self.nodes & other.nodes

def find_friends(u1, u2, friends, max_depth):
  frontiers = [Frontier(u1), Frontier(u2)]

  def advance_frontier(frontier):
    new_frontier = set()
    for user in frontier.nodes:
      path_to_user = frontier.paths[user]
      for user_friend in friends[user]:
        if user_friend not in frontier.paths:
          frontier.paths[user_friend] = path_to_user + [user]
          new_frontier.add(user_friend)
    frontier.nodes = new_frontier

  curr_depth = 1
  while True:
    frontier_intesection = frontiers[0] & frontiers[1]
    if frontier_intesection:
      connecting_node = frontier_intesection.pop()
      return (frontiers[0].paths[connecting_node] +
              [connecting_node] + 
              frontiers[1].paths[connecting_node][::-1])
    if curr_depth >= max_depth:
      break
    advance_frontier(frontiers[curr_depth % 2])
    curr_depth += 1
  return []
      
