def find_friends(u1, u2, friends, max_depth):
  class frontier(object):
    def __init__(self, start_node):
      self.nodes = set([start_node])
      self.paths = {start_node: []}

    def __and__(self, other):
      return self.nodes & other.nodes

  frontiers = [frontier(u1), frontier(u2)]

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
      
