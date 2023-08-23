# date: 06/08/2023

from a3_maze import Maze, print_mazefile, print_pathfile 

def find_path(the_maze, startCell, endCell):
    numOfRows = the_maze.get_num_rows()
    numOfCols = the_maze.get_num_cols()
    visited = [[False] * numOfCols for _ in range(numOfRows)]
    queue = [(startCell, [])]

    while queue:
        current_cell, path = queue.pop(0)
        row = the_maze.get_row(current_cell)
        col = the_maze.get_col(current_cell)

        if current_cell == endCell:
            return path + [current_cell]

        if not visited[row][col]:
            visited[row][col] = True

            
            left_cell = the_maze.get_left(current_cell)
            if left_cell != -1:
                queue.append((left_cell, path + [current_cell]))

            
            right_cell = the_maze.get_right(current_cell)
            if right_cell != -1:
                queue.append((right_cell, path + [current_cell]))

            
            up_cell = the_maze.get_up(current_cell)
            if up_cell != -1:
                queue.append((up_cell, path + [current_cell]))

            
            down_cell = the_maze.get_down(current_cell)
            if down_cell != -1:
                queue.append((down_cell, path + [current_cell]))

    return []  
