from abstract_collection import AbstractCollection
from arrays import Array
from grid import Grid
from stacks import LinkedStack
from queues import LinkedQueue

INF = "-"


def add_with_inf(a, b):
    return INF if (a == INF or b == INF) else a + b


def is_less_with_inf(a, b):
    if (a == INF):
        return False
    elif (b == INF):
        return True
    else:
        return a < b


def min_with_inf(a, b):
    if (a == INF):
        return b
    elif (b == INF):
        return a
    else:
        return min(a, b)


class LinkedVertex(object):
    """
    Represents the vertex in LinkedDirectedGraph.
    """

    def __init__(self, label):
        self.label = label
        self.edge_list = list()
        self.mark = False

    def __str__(self):
        return str(self.label)

    def __repr__(self):
        return f"Vertex({str(self)})"

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        return self.label == other.label

    def clear_mark(self):
        self.mark = False

    def set_mark(self):
        self.mark = True

    def is_marked(self):
        return self.mark

    def get_label(self):
        return self.label

    def set_label(self, label, g):
        """
        Sets the vertex's label to g's label.
        """
        g.vertices.pop(self.label, None)
        g.vertices[label] = self
        self.label = label

    def add_edge_to(self, to_vertex, weight):
        """
        Adds an edge to the to_vertex with a given weight.
        """
        if self.has_edge_to(to_vertex):
            raise AttributeError(f"Edge to {to_vertex} already exists.")
        edge = LinkedEdge(self, to_vertex, weight)
        self.edge_list.append(edge)

    def has_edge_to(self, to_vertex):
        """
        Returns True if the edge to the to_vertex exists, or False otherwise.
        """
        return bool(self.get_edge_to(to_vertex))

    def get_edge_to(self, to_vertex):
        """
        Returns the edge object to the to_vertex if exists, or False otherwise.
        """
        for edge in self.edge_list:
            if to_vertex == edge.get_other_vertex(self):
                return edge
        return False

    def remove_edge_to(self, to_vertex):
        """
        Returns True is the edge is removed successfully, or False otherwise.
        """
        for edge in self.edge_list:
            if edge.get_other_vertex(self) == to_vertex:
                self.edge_list.remove(edge)
                return True
        return False

    def incident_edges(self):
        """
        Returns an iterator of all edges coming out of self.
        """
        return iter(self.edge_list)

    def neighboring_vertices(self):
        """
        Returns an iterator of all neighboring vertices of self.
        """
        result = list()
        for edge in self.incident_edges():
            result.append(edge.get_other_vertex(self))
        return iter(result)


class LinkedEdge(object):
    """
    Represents the edge in LinkedDirectedGraph.
    """

    def __init__(self, from_vertex, to_vertex, weight=None):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight
        self.mark = False

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        return all([
            self.from_vertex == other.from_vertex,
            self.to_vertex == other.to_vertex,
            self.weight == other.weight
        ])

    def __str__(self):
        return f"{self.from_vertex}>{self.to_vertex}:{self.weight}"

    def __repr__(self):
        return f"Edge({str(self)})"

    def __hash__(self):
        return hash(str(self))

    def clear_mark(self):
        self.mark = False

    def set_mark(self):
        self.mark = True

    def is_marked(self):
        return self.mark

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_other_vertex(self, vertex):
        return self.to_vertex if vertex == self.from_vertex else self.from_vertex

    def get_from_vertex(self):
        return self.from_vertex

    def get_to_vertex(self):
        return self.to_vertex


class LinkedDirectedGraph(AbstractCollection):
    """
    A weighted directed graph implementation
    based on adjacency list.
    """

    # Constructor
    def __init__(self, source_collection=None):
        """
        size attribute counts the number of vertices.
        edge_count attribute counts the number of edges.
        vertices: {vertex name: vertex object}
        """
        self.edge_count = 0
        self.vertices = dict()
        AbstractCollection.__init__(self, source_collection)

    # Accessors
    def __str__(self):
        """
        Returns the string representation of self.
        """
        vertices_line = f"{len(self)} vertices: " + ", ".join(map(str, self.get_vertices())) + "\n"
        edges_line = f"{self.edge_count} edges: " + ", ".join(map(str, self.edges()))
        return vertices_line + edges_line

    def __iter__(self):
        """
        Supports iteration over the vertices in the graph.
        """
        return iter(self.vertices.values())

    def get_vertices(self):
        """
        Same as iter(self).
        """
        return iter(self)

    def edges(self):
        """
        Supports iteration over the edges in the graph.
        """
        result = set()
        for vertex in self.get_vertices():
            edges = vertex.incident_edges()
            result = result.union(set(edges))
        return iter(result)

    def size_vertices(self):
        """
        Returns the number of vertices in self.
        Same as len(self).
        """
        return len(self)

    def size_edges(self):
        """
        Returns the number of vertices in self.
        """
        return self.edge_count

    def contains_vertex(self, label):
        """
        Returns True if the label is in self, or False otherwise.
        """
        return label in self.vertices

    def get_vertex(self, label):
        """
        Returns the vertex object if the label is in self.
        Precondition: The label is in self.
        Raises AttributeError if the label is not in self.
        """
        vertex = self.vertices.get(label, None)
        if vertex is None:
            raise AttributeError(f"Vertex {label} is not in the graph.")
        return vertex

    def contains_edge(self, from_label, to_label):
        """
        Returns True if the edge is in self, or False otherwise.
        """
        from_vertex = self.get_vertex(from_label)
        to_vertex = self.get_vertex(to_label)
        return from_vertex.has_edge_to(to_vertex)

    def get_edge(self, from_label, to_label):
        """
        Returns the edge object if the edge is in self, or None otherwise.
        """
        from_vertex = self.get_vertex(from_label)
        to_vertex = self.get_vertex(to_label)
        return from_vertex.get_edge_to(to_vertex)

    def neighboring_vertices(self, label):
        """
        Returns all neighboring vertices of the vertex with the label exists,
        or None otherwise.
        """
        vertex = self.get_vertex(label)
        return vertex.neighboring_vertices() if vertex is not None else None

    def get_label_table(self):
        """
        Returns a dictionary with labels as keys and numbers as values.
        """
        label_table = dict()
        for k, v in enumerate(self):
            label_table[v.get_label()] = k
        return label_table

    def topological_sort(self):
        """
        Returns a list of vertices after topological sorting.
        """
        # Helper function
        def dfs(v, stack):
            v.set_mark()
            for w in self.neighboring_vertices(v.get_label()):
                if not w.is_marked():
                    dfs(w, stack)
            stack.push(v)

        stack = LinkedStack()
        self.clear_vertex_marks()
        for v in self.get_vertices():
            if not v.is_marked():
                dfs(v, stack)
        result = []
        while not stack.is_empty():
            result.append(stack.pop())
        return result

    def depth_first(self, start_label):
        """
        Traverse the graph from the starting vertex using DFS.
        Returns a list of vertices.
        """
        # Helper function
        def recurse(stack, result):
            if stack.is_empty():
                return
            v = stack.peek()
            for w in v.neighboring_vertices():
                if not w.is_marked():
                    w.set_mark()
                    stack.push(w)
                    result.append(w)
                    recurse(stack, result)
            stack.pop()

        stack = LinkedStack()
        self.clear_vertex_marks()
        v = self.get_vertex(start_label)
        v.set_mark()
        stack.add(v)
        result = [v]
        recurse(stack, result)
        return result

    def breadth_first(self, start_label):
        """
        Traverse the graph from the starting vertex using BFS.
        Returns a list of vertices.
        """
        self.clear_vertex_marks()
        queue = LinkedQueue()
        # Initialize
        start_vertex = self.get_vertex(start_label)
        start_vertex.set_mark()
        result = [start_vertex]
        queue.add(start_vertex)
        while not queue.is_empty():
            # Get the front vertex and its edge to other vertices
            # Add all non-marking vertices to the queue.
            v = queue.pop()
            for edge in v.incident_edges():
                to_vertex = edge.get_to_vertex()
                if not to_vertex.is_marked():
                    result.append(to_vertex)
                    queue.add(to_vertex)
                    to_vertex.set_mark()
        return result

    def span_tree(self, start_label):
        """
        Returns the minimal spanning tree using Prim algorithm.
        """
        # Helper function
        def find_minimal_weight_edge(visited_edges, visited, not_visited):
            minimal_edge = None
            minimal_weight = INF
            for edge in self.edges():
                if all([
                    edge not in visited_edges,
                    edge.get_from_vertex() in visited,
                    edge.get_to_vertex() in not_visited,
                ]):
                    weight = edge.get_weight()
                    if is_less_with_inf(weight, minimal_weight):
                        minimal_edge = edge
                        minimal_weight = weight
            return minimal_edge
        # Clear all marks for both vertices and edges.
        self.clear_vertex_marks()
        self.clear_edge_marks()
        # Mark the starting vertex as visited.
        start_vertex = self.get_vertex(start_label)
        start_vertex.set_mark()
        # Starting the algorithm
        visited = set([start_vertex])
        not_visited = set(self) - visited
        tree_edges = set()
        for vertex in self:
            min_weight_edge = find_minimal_weight_edge(tree_edges, visited, not_visited)
            if min_weight_edge is None:
                return list(tree_edges)
            else:
                w = min_weight_edge.get_to_vertex()
                min_weight_edge.set_mark()
                w.set_mark()
                visited.add(w)
                not_visited.remove(w)
                tree_edges.add(min_weight_edge)

    def shortest_paths(self, start_label):
        """
        Returns the shortest paths from starting vertex using Dijkstra algorithm.
        """
        included = Array(len(self))
        result = Grid(len(self), 3)
        start_vertex = self.get_vertex(start_label)
        # Initializing
        num = 0
        for vertex in self:
            result[num][0] = vertex.get_label()
            if vertex == start_vertex:
                # If it's the starting vertex
                result[num][1] = 0
                result[num][2] = None
                included[num] = True
            elif start_vertex.has_edge_to(vertex):
                # If it's connecting to the starting vertex
                result[num][1] = start_vertex.get_edge_to(vertex).get_weight()
                result[num][2] = start_vertex
                included[num] = False
            else:
                # Other vertices
                result[num][1] = INF
                result[num][2] = None
                included[num] = False
            num += 1
        # Computing
        while True:
            # Find the vertex that hasn't been included and
            # has the minimal distance in the result grid.
            # Break if all vertices have been included.
            min_num = None
            min_dist = INF
            for num in range(len(self)):
                dist = result[num][1]
                if not included[num] and is_less_with_inf(dist, min_dist):
                    min_num = num
                    min_dist = dist
            if min_num is None:
                break
            # Mark this vertex as visited
            included[min_num] = True
            for other_num in range(len(self)):
                this_label = result[min_num][0]
                other_label = result[other_num][0]
                edge = self.get_edge(this_label, other_label)
                if not included[other_num] and edge:
                    new_dist = add_with_inf(edge.get_weight(), result[min_num][1])
                    if is_less_with_inf(new_dist, result[other_num][1]):
                        result[other_num][1] = new_dist
                        result[other_num][2] = this_label
        return result

    def has_path(self, start_label, to_label):
        """
        Returns True if there's a path between two vertices, or False otherwise.
        """
        if not all([self.contains_vertex(start_label), self.contains_vertex(to_label)]):
            return False
        # Using BFS to search possible routes
        # Break if encounters the target during the search
        self.clear_vertex_marks()
        queue = LinkedQueue()
        start_vertex = self.get_vertex(start_label)
        target_vertex = self.get_vertex(to_label)
        start_vertex.set_mark()
        result = [start_vertex]
        queue.add(start_vertex)
        while not queue.is_empty():
            # Get the front vertex and its edge to other vertices
            # Add all non-marking vertices to the queue.
            v = queue.pop()
            for edge in v.incident_edges():
                to_vertex = edge.get_to_vertex()
                if to_vertex == target_vertex:
                    return True
                if not to_vertex.is_marked():
                    result.append(to_vertex)
                    queue.add(to_vertex)
                    to_vertex.set_mark()
        to_vertex = self.get_vertex(to_label)
        accessible_vertices = self.breadth_first(start_label)
        return to_vertex in accessible_vertices[1:]

    def get_distance_matrix(self):
        """
        Returns the adjacency matrix of the graph.
        """
        dist_matrix = Grid(len(self), len(self), INF)
        label_table = self.get_label_table()
        for from_vertex in self:
            from_label = from_vertex.get_label()
            row = label_table[from_label]
            for to_vertex in from_vertex.neighboring_vertices():
                to_label = to_vertex.get_label()
                col = label_table[to_label]
                edge = self.get_edge(from_label, to_label)
                dist_matrix[row][col] = edge.get_weight()
            dist_matrix[row][row] = 0
        return dist_matrix

    def get_all_pairs_shortest_paths(self):
        """
        Returns the shortest paths between all pairs of vertices using Floyd algorithm.
        """
        dist_matrix = self.get_distance_matrix()
        for k in range(len(self)):
            for r in range(len(self)):
                for c in range(len(self)):
                    dist_matrix[r][c] = min_with_inf(
                        dist_matrix[r][c],
                        add_with_inf(dist_matrix[r][k], dist_matrix[k][c])
                    )
        return dist_matrix

    # Mutators
    def clear(self):
        """
        Makes self become empty.
        """
        self.edge_count = 0
        self.size = 0
        self.vertices = dict()

    def clear_edge_marks(self):
        """
        Removes all edge marks.
        """
        for edge in self.edges():
            edge.clear_mark()

    def clear_vertex_marks(self):
        """
        Removes all vertex marks.
        """
        for vertex in self:
            vertex.clear_mark()

    def add_vertex(self, label):
        """
        Adds the vertex to self.
        Precondition: The label is not in self.
        Raises AttributeError if the label is in self.
        """
        if self.contains_vertex(label):
            raise AttributeError(f"Vertex {label} is already in the graph.")
        self.vertices[label] = LinkedVertex(label)
        self.size += 1

    def add(self, label):
        """
        Same as self.add_vertex(label).
        """
        return self.add_vertex(label)

    def remove_vertex(self, label):
        """
        Returns True is the vertex is removed successfully, or False otherwise.
        """
        removed_vertex = self.vertices.pop(label, None)
        if removed_vertex is None:
            return False
        else:
            # Remove all edges to the removed vertex:
            for vertex in self.get_vertices():
                if vertex.remove_edge_to(removed_vertex):
                    self.edge_count -= 1
            # Remove all edges from the removed vertex:
            for edge in removed_vertex.incident_edges():
                self.edge_count -= 1
            # Decrease the vertex count by 1
            self.size -= 1
            return True

    def add_edge(self, from_label, to_label, weight=None):
        """
        Adds the edge to self.
        Precondition: The label is not in self.
        Raises AttributeError if the label is in self.
        """
        if self.contains_edge(from_label, to_label):
            raise AttributeError(f"Edge {from_label}>{to_label} is already in the graph.")
        from_vertex = self.get_vertex(from_label)
        to_vertex = self.get_vertex(to_label)
        from_vertex.add_edge_to(to_vertex, weight)
        self.edge_count += 1

    def remove_edge(self, from_label, to_label):
        """
        Returns True is the edge is removed successfully, or False otherwise.
        """
        from_vertex = self.get_vertex(from_label)
        to_vertex = self.get_vertex(to_label)
        removed_edge_flag = from_vertex.remove_edge_to(to_vertex)
        if removed_edge_flag:
            self.edge_count -= 1
        return removed_edge_flag
