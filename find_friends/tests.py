import unittest
from unittest import TestCase
from find_friends_dfs import find_friends as find_friends_dfs
from find_friends_bfs import find_friends as find_friends_bfs
from find_friends_bfs import find_friends2 as find_friends_bfs_with_dict
from find_friends_bfs import find_friends3 as find_friends_bfs_lists
from find_friends_set_intersection import find_friends as find_friends_sets

class SimpleFriendGraph(TestCase):
  def setUp(self):
    self.friends = {
      1: set([2,]),
      2: set([1,5,3]),
      3: set([2,6,4]),
      4: set([3,6]),
      5: set([2]),
      6: set([3,4]),
      7: set([])
    }

    self.algos_to_test = [
      find_friends_dfs,
      find_friends_bfs,
      find_friends_bfs_with_dict,
      find_friends_bfs_lists,
      find_friends_sets,
    ]

  def test_self_friend(self):
    for algo in self.algos_to_test:
      self.assertListEqual(algo(1,1,self.friends, 3), [1])

  def test_friend(self):
    for algo in self.algos_to_test:
      self.assertListEqual(algo(1,2,self.friends, 3), [1,2])

  def test_friend_of_friend(self):
    for algo in self.algos_to_test:
      self.assertListEqual(algo(1,3,self.friends, 3), [1,2,3])

  def test_third_degree_friend(self):
    for algo in self.algos_to_test:
      self.assertListEqual(algo(1,4,self.friends, 4), [1,2,3,4])

  def test_friend_too_far_away(self):
    for algo in self.algos_to_test:
      self.assertListEqual(algo(1,4,self.friends, 3), [])

  def test_isolated_friend(self):
    for algo in self.algos_to_test:
      self.assertListEqual(algo(1,7,self.friends, 3), [])

  def test_shortest_path(self):
    for algo in self.algos_to_test:
      self.assertListEqual(algo(6,4,self.friends, 3), [6,4])


