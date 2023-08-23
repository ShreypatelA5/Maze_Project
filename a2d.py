# date: 06/08/2023
class Graph:

    def check_valid_vertex(self, v):
        return 0 <= v < self.number_of_verts
    
    def __init__(self, number_of_verts):
        self.number_of_verts = number_of_verts
        self.edge_list = [[] for _ in range(number_of_verts)]

    def add_vertex(self):
        self.number_of_verts += 1
        self.edge_list.append([])

    def add_edge(self, from_idx, to_idx, weight=1):
        if not self.check_valid_vertex(from_idx) or not self.check_valid_vertex(to_idx):
            return False

        if self.has_edge(from_idx, to_idx):
            return False

        self.edge_list[from_idx].append((to_idx, weight))
        return True

    def num_edges(self):
        countNo = 0
        for edgesNo in self.edge_list:
            countNo += len(edgesNo)
        return countNo

    def num_verts(self):
        return self.number_of_verts

    def has_edge(self, from_idx, to_idx):
        if not self.check_valid_vertex(from_idx) or not self.check_valid_vertex(to_idx):
            return False

        for vertexIndex, _ in self.edge_list[from_idx]:
            if vertexIndex == to_idx:
                return True
        return False

    def edge_weight(self, from_idx, to_idx):
        if not self.check_valid_vertex(from_idx) or not self.check_valid_vertex(to_idx):
            return None

        for vertexIndex, weightNo in self.edge_list[from_idx]:
            if vertexIndex == to_idx:
                return weightNo
        return None

    def get_connected(self, v):
        if not self.check_valid_vertex(v):
            return []

        return self.edge_list[v]
        
    def get_vertices(self):
        return list(range(self.number_of_verts))

    def get_edges(self):
        edges = []
        for from_idx in range(self.number_of_verts):
            for to_idx, weight in self.edge_list[from_idx]:
                edges.append((from_idx, to_idx, weight))
        return edges
    