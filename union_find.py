#!/usr/bin/env python3

class UnionFind:
    def __init__(self, init=[]):
        self.rank = {}
        self.parents = {}
        for x in init:
            self.add(x)
        
    def add(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.rank[x] = 1
            
    def find(self, x):
        if self.parents[x] == x:
            return x
        
        elif self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def contains(self, x):
        return x in self.parents
        
    def setSize(self, x):
        return self.rank[self.parents[x]]
        
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        
        if x_parent != y_parent:
            if self.rank[x_parent] >= self.rank[y_parent]:
                self.parents[y_parent] = self.parents[x_parent]
                self.rank[x_parent] += self.rank[y_parent]
            else:
                self.parents[x_parent] = self.parents[y_parent]
                self.rank[y_parent] += self.rank[x_parent]
            
    def sets(self):
        parent_map = {}
        for x in self.parents.keys():
            parent = self.find(x)
            if parent not in parent_map:
                parent_map[parent] = [x]
                
            else:
                parent_map[parent].append(x)
                
        return parent_map.values()

