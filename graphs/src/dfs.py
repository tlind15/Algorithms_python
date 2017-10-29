from graph import Graph, rand_graph
from collections import deque


def dfs(graph, start):
    if start < 0 or start >= graph.size():  # if they pick a start node this isn't in the graph
        return None

    visited = [start]  # we start having visited the starting point
    reachable = deque([])  # will show all reachable vertices
    pointer = 0  # will represent position in the visited list. It will mimic a stack while also retaining visit history

    times = {}  # will shoe all nodes plus their start and end times
    for i in range(graph.size()): # put node values in dictionary
        times[i] = []
    t = 1  # we start at time = 1
    while pointer >= 0: # while the starting node has not ended
        if len(times[visited[pointer]]) == 0:  # if the node being visited does not not have a starting time
            times[visited[pointer]].append(t)
        t += 1  # increment time for next action
        neighbors = graph.show_paths_out(visited[pointer])  # explore the vertex and find neighbors

        # this construct will find the highest priority neighbors
        # this algorithm priorities neighbors based on the vertex value. The lowest vertices have highest priority
        # find priority by sorting the list of neighbors by their vertex value and pick the lowest one that we haven't already visited
        neighbors.sort()
        for n in neighbors:
            # if the vertex we are exploring has at least one neighbor and we have not visited it
            if n is not None and n not in visited:
                visited.append(n)  # add vertex to visited list
                pointer = len(visited) - 1  # pointer will move to top of 'stack'
                break

        # else structure will call if we did not reach the break statement
        # this indicates that the vertex is a dead end
        else:
            # check to make sure the current node has not already been reached by some other path
            # make sure we don't include that node twice if part of a loop
            if (visited[pointer]) not in reachable:
                reachable.appendleft(visited[pointer])
                times[visited[pointer]].append(t)  # set the end time for the node

            # we don't want to give the current vertex another end time if it already has one. And we don't want to skip end times
            else:
                t -= 1
            pointer -= 1  # we back track

    print("These are the reachable vertices from %s using DFS" % start, reachable)  # prints list of all reachable nodes
    return times  # prints dictionary of each node and its start/end times. If it is not reachable it has no times at all.




