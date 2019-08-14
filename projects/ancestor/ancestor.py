from util import Queue



def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    visited = set()
    count = 0
    
    q.enqueue([starting_node])

    # will return false if the size is less than 1
    while q.size():
        child = q.dequeue
        visited.add(child)
        for edge in _____:
            if edge not in visited:
                q.enqueue(edge)
                count +=1
    return count

