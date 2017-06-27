"""QUESTION 3
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be question3(G)"""

parent = dict()
rank = dict()

#Function to make a tree subset
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

#Function to find the root of the path
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

#Function to combine tree subsets
def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]: 
                rank[r2] += 1

#Function to create the minimum spanning tree using path compression and Kruskals algorithm
def kruskalAlgorithm(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimumSpanningTree = []
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        w, v1, v2 = edge
        if find(v1) != find(v2):
            union(v1,v2)
            minimumSpanningTree.append(edge)

    return minimumSpanningTree

#Function taking in adjacency list graph and returning minimum spanning tree as an adjacency matrix
def question3(G):

    graph = {
        'vertices': G.keys(),
        'edges': []
    }

    for v in G:
        for u in xrange(0,len(G[v])):
            edge = (G[v][u][1],v,G[v][u][0])
            graph['edges'].append(edge)
    
    mst = kruskalAlgorithm(graph)

    adjList = {}
    for i in xrange(0,len(mst)):
        adjList[mst[i][1]] = [mst[i][2],mst[i][0]]

    return adjList

G = {'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

print question3(G)

#Efficiency O(n^2)