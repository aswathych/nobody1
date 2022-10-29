# GEO1000 - Assignment 2
# Authors:
# Studentnumbers:

from importlib.resources import path


def read_grid(filenm):
    """
    Return a nested list used by the visit function
    filenm: the name of the txt file
    return: a nested list; sublist represents a row; every cell stored as an integer tuple(row, col)
    """
    table = []
    with open(filenm, 'r') as f:
        text = f.readlines()
        for i in range(1, 11, 2):
            row = text[i]
            row_adjusted = row.rstrip().replace(' ', '').split('|')
            sublist = []
            for j in range(1, 6):
                sublist.append((int(row_adjusted[j][0]), int(row_adjusted[j][1])))
            table.append(sublist)
    return table


def visit(table, steps_allowed, path):
    """
    Append the cells and traverse throughout to the path list
    table: a nested list returned by the read_grid function
    steps_allowed: maximum steps for the search
    path: a solution list created by hunt function
    return: a boolean value based on whether the treasure is found
    """
    row_num = 0
    col_num = 0
    path.append((row_num, col_num))
    for i in range(steps_allowed):
        row_num = table[path[i][0]][path[i][1]][0]
        col_num = table[path[i][0]][path[i][1]][1]
        if path[i][0] == row_num and path[i][1] == col_num:
            return True
        path.append((row_num, col_num))
    return False


def hunt(filenm, max_steps):
    """
    Make an empty path list for the visit function and give hunting output
    filenm: the name of the txt file that contains the table
    max_steps: maximum steps for the search
    return: a string according to the outcome of function visit
    """
    table = read_grid(filenm)
    global path
    path = []
    if visit(table, max_steps, path):
        return 'The treasure was found at row: {0}, column: {1}; it took {2} steps to find the treasure.'.format(path[-1][0], path[-1][1], len(path))
    else:
        return 'Could not find a treasure (in {} steps)'.format(max_steps)


if __name__ == "__main__":
    print(hunt('finite.txt', 20))
