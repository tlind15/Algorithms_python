from graph import *
from bfs import bfs, paths_from_spanning
from dfs import dfs

print("Input the order: ")
order = int(input()) #takes in input

while order <= 0: #ensuring a valid size
    print("Not a valid size input a size: ")
    order = int(input())

print("Input the size: ")
size = int(input()) #takes in input

while size < 0: #ensuring a valid size
    print("Not a valid size input a size: ")
    size = int(input())

graph = rand_graph(order, size)

print("The generated graph")
graph.print()

print("Select the starting vertex: ")
start = int(input()) #takes in input

while start < 0: #ensuring a valid size
    print("Not a valid size input a size: ")
    start = int(input())

print("These are the paths from the start to each vertex using BFS",bfs(graph, start))
print(dfs(graph, start))
