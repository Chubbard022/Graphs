from util import Queue


class Graph:
    #represent a graph as a dictionary of vertices mapping labels to edges
    def __init__(self):
        self.vertices = {}

#using a set within add vertex will provide easy lookup and wont allow duplicates
    def add_vertex(self,vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            print("ERROR")
    def add_edge(self,vertex_from ,vertex_to):
        if vertex_from in self.vertices and vertex_to in self.vertices:
            self.vertices[vertex_from].add(vertex_to)
        else:
            print("ERROR")

def earliest_ancestor(ancestors, starting_node):
        #make a graph
    graph = Graph()
    
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        #add the edge
        graph.add_edge(pair[1],pair[0])

        #traverse the graph with BFS
        q = Queue()
        q.enqueue([starting_node,])

        max_path_length = 1
        earliest_ancestor = -1

        while q.size():
            path = q.dequeue()
            node = path[-1]
            
            if(len(path) > max_path_length or (len(path) == max_path_length and node < earliest_ancestor)):
                earliest_ancestor = node
                max_path_length = len(path)

            for neighbor in graph.vertices[node]:
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)


    #steps we need to do
    #make a graph
    #traverse the graph
        #looking for the shortest path between any two nodes
            #keep the track of the lengths of the paths 
    #return lonest path
    #if there are no parents, return -1
    #if there is a tie, return lowest node number

#key words in problem
    #relationships-- best solved with graph ---
    #farthest distance ---
    #each person has an integer ID --- (NODE)
    #parent child par --- (EDGES)
    #not all relationships are the same
    #only look up to an ancestor --- directional



