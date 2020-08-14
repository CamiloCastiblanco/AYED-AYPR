from sys import stdin
import math
from random import randint

class DisjointSet:
    def __init__(self):
        self.data = []
        
    def find(self, e):
        for st in self.data:
            if e in st :
                return st
        return None

    def findTuple(self, tuple):
        return (self.find(tuple[0]), self.find(tuple[1]))

    def insert(self, el):
        if self.find(el) is None :
            self.data.append(set([el]))

    def union(self, s1, s2):
        unionSet = s1.union(s2)
        self.data.remove(s1)
        if s1 != s2:
            self.data.remove(s2)
        self.data.append(unionSet)

    def buildDisjointSet(self, elements):
        for e in elements:
            self.insert(e)

    def getData(self):
        return self.data

    def calculateConnectedComponents(self, arcs):
        for pair in arcs:
            tupleSets = self.findTuple(pair)
            print('Computed pair:',pair,'Components Found:',tupleSets)
            self.union(tupleSets[0], tupleSets[1])
            print('Merge components:',self.data)

def main():
    n = int(stdin.readline().strip())
    arcs = []
    vertexes = []
    for i in range(n):
        x = [stdin.readline().strip().split(" ")]
        arcs += x
        print(arcs)
    for i in range(len(arcs)):
        for j in range(1):
            vertexes += arcs[i][j] 
        print(arcs)
    dset = DisjointSet()
    dset.buildDisjointSet(vertexes)
    print(dset.getData())
    dset.calculateConnectedComponents(arcs)
main()
