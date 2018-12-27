"""
Given a 2D grid, each cell is either a wall 'W',
an enemy 'E' or empty '0' (the number zero),
return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from
the planted point until it hits the wall since the wall is too strong
to be destroyed.
Note that you can only put the bomb at an empty cell.
Example:
For the given grid
0 E 0 0
E 0 W E
0 E 0 0
return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""

import numpy as np


def bomb_row(row, index):
    kills = 0
    step = index
    while step > 0:
        step -= 1
        if row[step] == "e":
            kills += 1
        elif row[step] == "w":
            break

    step = index
    while step < len(row)-1:
        step += 1
        if row[step] == "e":
            kills += 1
        elif row[step] == "w":
            break

    return kills


def bomb_enemy(grid):
    kills = 0
    for i, row in enumerate(grid):
        for j, elm in enumerate(row):
            if elm == "0":
                kills = max(kills, bomb_row(row, j)+bomb_row(grid[:, j], i))

    return kills


if __name__ == "__main__":
    grid = np.asarray([[0, "e", 0, 0, "e"],
                       ["e", 0, "e", "w", "e"],
                       [0, "e", 0, 0, 0],
                       [0, "e", 0, 0, 0]
                       ])
    assert bomb_enemy(grid) == 5
