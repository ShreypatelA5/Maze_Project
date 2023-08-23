import random
from a2d import Graph
from a3_partb import minimum_spanning_tree

def generate_maze(numRows, numCols):
    # Maze total number of cells 
    TCells = numRows * numCols

    # Create a tuple list of walls
    walls = []
    for row in range(numRows):
        for col in range(numCols):
            # find the index of the maze current cell
            indexCell = row * numCols + col

            # insert right wall between the right neighbouring part 
            if col + 1 < numCols:
                indexRightneighbor = row * numCols + (col + 1)
                walls.append((indexCell, indexRightneighbor))

            # insert down wall between the down neighbouring part
            if row + 1 < numRows:
                indexDownneighbor = (row + 1) * numCols + col
                walls.append((indexCell, indexDownneighbor))

    # graphical representation of maze
    maze_graph = Graph(TCells)

    # random weight having edges are created
    for from_idx, to_idx in walls:
        # Generates a random edge weight between 1 and 50
        randWeight = random.randint(1, 50)

        # with the random weight edge is added between neighbors
        maze_graph.add_edge(from_idx, to_idx, randWeight)

        # Due to undirected nature of graph, reverse edge is added
        maze_graph.add_edge(to_idx, from_idx, randWeight)

    # minimum spanning tree is identified using Kruskal's algorithm 
    edgesOfMst = minimum_spanning_tree(maze_graph)

    # To create final maze removal of the MST edges from the list of walls 
    final_walls = [wall for wall in walls if wall not in edgesOfMst]

    return final_walls

if __name__ == '__main__':
    # Exempler maze creation: rows = 3, columns = 4.
    maze_walls = generate_maze(3, 4)
    print(maze_walls)