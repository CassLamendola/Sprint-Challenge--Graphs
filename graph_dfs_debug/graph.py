"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        explored = set()

        while stack:
            vertex = stack.pop()
            if vertex not in explored:
                explored.add(vertex)
                if vertex == target:
                    break
                stack.extend(self.vertices[vertex])
        return explored

    def graph_rec(self, start, target=None, explored=None):
        explored = explored or set()
        explored.add(start)
        if start == target:
            return explored
        for vertex in self.vertices[start]:
            if vertex not in explored:
                self.graph_rec(vertex, target=target, explored=explored)
        return explored

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
