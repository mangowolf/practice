"""Graph Representation Practice"""

#Class defining the node object for the graph
class Node(object):
    """Initialize the object with base values"""
    def __init__(self,value):
        self.value = value
        self.edges = []

#Class defining the Edge objects for the graph
class Edge(object):
    """Initialize the object with base value"""
    def __init__(self, value, node_from, node_to): 
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

#Class defining the graph
class Graph(object):
    """Initialize the graph object with base values"""
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    """Function to create and insert new node into graph node array"""
    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    """Function to create and insert new edge connection between nodes into
    graph object edge array"""
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(new_edge_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(new_edge_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edge_list = []
        for edge_object in self.edges:
            edge = (edge_object.value, edge_object.node_from.value, edge_object.node_to.value)
            edge_list.append(edge)
            print edge

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)

print graph.get_edge_list()