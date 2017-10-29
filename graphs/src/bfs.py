from graph import Graph, rand_graph
from collections import deque


def bfs(graph, start):
    if start < 0 or start >= graph.size():
        return None

    visited = [start]  # list to keep track of where we have visited
    spanning = {} # an array of dictionaries that will serve as spanning tree representation
    pointer = 0 # will represent position in list visited
    while pointer < graph.size(): # while we have yet to check out the neighbors for each node

        neighbors = graph.show_paths_out(visited[pointer]) # gets neighbors of a node
        spanning[visited[pointer]] = [] # each dictionary entry will show a node and its children in the spanning tree
        size_i = len(visited) # initial size before elements are added
        for n in neighbors: # each neighbors in the list of neighbors
            if n is not None and n not in visited: # if the node has a neighbor and we haven't already visited it
                visited.append(n) # add that neighbor to the visited list
                spanning[visited[pointer]].append(n) # add that node as a child of the current node in the spanning tree

        # if the siz_i and current size are the same that means no new nodes were added
        # this means either every node has been visited or the graph is not connected and there isn't an edge to an unvisited node
        if size_i == len(visited):
            # find the lowest vertex number that has not been visited and go there
            for i in range(graph.size()):
                if i not in visited:
                    visited.append(i) # add that node to visited
                    break

        pointer += 1 #increment pointer to check out the neighbors of the neighbors in the next iteration

    print(spanning)
    return paths_from_spanning(spanning, start)


def paths_from_spanning(tree, start):
    temp = start
    paths = []
    traveled = [start]
    while len(tree[start]) > 0:
        if len(tree[temp]) > 0:  # if the vertex of interest has neighbors that haven't been printed
            traveled.append(tree[temp][0])  # add to top of stack
            temp = traveled[-1]  # temp is top of stack

        else:
            paths.append(list(traveled))
            holder = traveled.pop()  # pop top off stack and set it equal to holder to remove from spanning tree
            temp = traveled[-1]  # temp is top of stack
            tree[temp].remove(holder)  # remove element that we popped

    return paths

