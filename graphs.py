#!/usr/bin/env python3
# graphs.py
# some graph algorithms

from typing import *
from heap import Heap

def buildAdjacencyList(g):
  adj = {}
  for (source, target, cost) in g:
    if source not in adj:
      adj[source] = [(target, cost)]

    else:
      adj[source].append((target, cost))

  return adj

# Dijkstra's algorithm
# this implementation is more complicated than it should be because the
# implementation of min-heap that we use does not support updating the
# cost of a current node; instead, we track the minimum cost in cost_map
# and add duplicate nodes to the heap, and track nodes that have been visited
# with the visited set
def dijkstra(g, start, goal=None):
  adj = buildAdjacencyList(g)

  # set of visited nodes
  cost_map = {}
  visited = set()
  frontier = Heap()

  frontier.insert(start, 0)
  while frontier.size() > 0:
    cur_node, cur_cost = frontier.extractMin()

    # nodes might be added multiple times in the frontier since we don't
    # update the node weights but add copies of the node with smaller costs
    if cur_node in visited:
      continue

    # if the current node is the goal, then stop
    # to find the shortest path from start to *any* node, remove this condition
    if cur_node == goal:
      break

    visited.add(cur_node)
    neighbors = [] if cur_node not in adj else adj[cur_node]
    for (neighbor, edge_cost) in neighbors:
      if neighbor not in visited:
        new_cost = cur_cost + edge_cost
        if neighbor not in cost_map or cost_map[neighbor][0] > new_cost:
          cost_map[neighbor] = (new_cost, cur_node)
          frontier.insert(neighbor, new_cost)

  # build path from
  if goal is not None:
    path = []
    path_node = goal
    while path_node != start:
      path.insert(0, path_node)
      _, path_node = cost_map[path_node]

    path.insert(0, start)
      
    return path

  # return set of minimum paths from start to all other nodes
  else:
    paths = set()
    for node in visited:
      if node is not start:
        _, parent = cost_map[node]
        paths.add((parent, node))
      
    return paths

# Prim's algorithm for MST
# very similar to Dijkstra, except the weights of nodes in the frontier are
# given by the cost of the edge spanning the node, NOT the node's distance
def prims(g, root):
  adj = buildAdjacencyList(g)

  # set of visited nodes
  cost_map = {}
  visited = set()
  frontier = Heap()

  frontier.insert(root, 0)
  while frontier.size() > 0:
    cur_node, cur_cost = frontier.extractMin()

    # nodes might be added multiple times in the frontier since we don't
    # update the node weights but add copies of the node with smaller costs
    if cur_node in visited:
      continue

    visited.add(cur_node)
    neighbors = [] if cur_node not in adj else adj[cur_node]
    for (neighbor, edge_cost) in neighbors:
      if neighbor not in visited:
        # this is basically the only difference to Dijkstra's:
        # the cost is *just* the edge cost, not the cost of the cur_node + edge
        new_cost = edge_cost

        if neighbor not in cost_map or cost_map[neighbor][0] > new_cost:
          cost_map[neighbor] = (new_cost, cur_node)
          frontier.insert(neighbor, new_cost)

  # build MST
  mst = set()
  for node in visited:
    if node is not root:
      _, parent = cost_map[node]
      mst.add((parent, node))
    
  return mst


# Kruskal's algorithm for MST
def kruskal(g):
  nodeset_map = {}
  nodes = set()
  frontier = Heap()

  for (source, target, cost) in g:
    frontier.insert((source, target), cost)
    nodes.add(source)
    nodes.add(target)

  for node in nodes:
    nodeset_map[node] = node

  mst = set()
  num_nodesets = len(nodes)
  while num_nodesets > 1 and frontier.size() > 0:
    e, _ = frontier.extractMin()

    # nodes are already part of the same forest; don't add edge
    if nodeset_map[e[0]] == nodeset_map[e[1]]:
      continue

    else:
      mst.add(e)
      num_nodesets -= 1

      # union by adding target nodeset to source nodeset
      source_nodeset, target_nodeset = nodeset_map[e[0]], nodeset_map[e[1]]
      for node in nodes:
        if nodeset_map[node] == target_nodeset:
          nodeset_map[node] = source_nodeset

  return mst


def testGraph():
  g = [(1,2,5),(1,3,5),(1,4,5),(2,3,1),(3,4,1)]
  path = dijkstra(g, 1, 3)
  paths = dijkstra(g, 1)
  mst = prims(g, 1)
  mst2 = kruskal(g)
  print("path from 1 to 3:", path)
  print("paths from 1:", paths)
  print("MST with root 1", mst)
  print("Kruskal's MST", mst2)

if __name__ == '__main__':
  testGraph()
