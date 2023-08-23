from a2d import Graph

class DisjointSet:
    def __init__(self, elements):
        self.representative = {element: element for element in elements}
        self.tree_rank = {element: 0 for element in elements}

    def locate(self, item):
        if self.representative[item] != item:
            self.representative[item] = self.locate(self.representative[item])
        return self.representative[item]

    def union(self, item1, item2):
        root1 = self.locate(item1)
        root2 = self.locate(item2)
        if root1 != root2:
            if self.tree_rank[root1] < self.tree_rank[root2]:
                self.representative[root1] = root2
            elif self.tree_rank[root1] > self.tree_rank[root2]:
                self.representative[root2] = root1
            else:
                self.representative[root2] = root1
                self.tree_rank[root1] += 1


def minimum_spanning_tree(graph):
    mst = []
    elements = graph.get_vertices()
    unique_disjoint_set = DisjointSet(elements)
    sorted_links = sorted(graph.get_edges(), key=lambda link: link[2])

    for link in sorted_links:
        src, dest, weight = link
        if unique_disjoint_set.locate(src) != unique_disjoint_set.locate(dest):
            mst.append((src, dest))
            unique_disjoint_set.union(src, dest)

    return mst
