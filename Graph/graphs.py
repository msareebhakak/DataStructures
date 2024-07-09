#
# Author: Sareeb Hakak
# Purpose: Learn Graph DS
# Date: 01 March 2024
#

from collections import deque


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for edge in self.edges:
            self.add_edge(edge)
        print(f'Graph Dict created is \n {self.graph_dict}')

    def add_edge(self, edge):
        start = edge[0]
        end = edge[1]
        if start in self.graph_dict.keys():
            self.graph_dict[start].append(end)
        else:
            self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict.keys():
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path

        if start not in self.graph_dict.keys():
            return []

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_paths(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

    def bfs(self, s):
        graph_queue = deque()
        graph_queue.append(s)
        visited = []

        while graph_queue:
            node = graph_queue.popleft()
            if node not in visited:
                visited.append(node)

            if node in self.graph_dict.keys():
                for vals in self.graph_dict[node]:
                    if vals not in visited:
                        graph_queue.append(vals)

        return visited

    def dfs(self, s):
        graph_stack = deque()
        graph_stack.append(s)
        visited = []

        while graph_stack:
            node = graph_stack.pop()
            if node not in visited:
                visited.append(node)

            if node in self.graph_dict.keys():
                for vals in reversed(self.graph_dict[node]):
                    if vals not in visited:
                        graph_stack.append(vals)

        return visited


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route = Graph(routes)
    print(route.bfs("Mumbai"))
    print(route.dfs("Mumbai"))

    print(f"Paths b/w Mumbai and Toronto: ", route.get_paths("Mumbai", "Toronto"))
    print(f"Shortest path b/w Mumbai and Toronto: ", route.shortest_path("Mumbai", "Toronto"))
