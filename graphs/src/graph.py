from random import randint


class Graph:
    def __init__(self, num_nodes):
        self.nodes = [[] for x in range(num_nodes)]

    def add_path(self, startnode, endnode):
        self.nodes[startnode].append(endnode)

    def remove_path(self, startnode, endnode):
        self.nodes[startnode].remove(endnode)

    def show_paths_out(self, node):
        self.nodes[node].sort()
        return self.nodes[node]

    def path_exists(self, start, end):
        if end in self.nodes[start]:
            return True
        else:
            return False

    def size(self):
        return len(self.nodes)

    def print(self):
        for i in range(self.size()):
            self.nodes[i].sort()
            print(i, self.nodes[i])


def rand_graph(order, size):
    graph = Graph(order)

    start = None
    end = None
    count = 0
    while count < size:
        start = randint(0, order-1)
        end = randint(0, order-1)

        if not graph.path_exists(start, end) and not graph.path_exists(end, start) and start != end:
            graph.add_path(start, end)
            count += 1

    return graph












