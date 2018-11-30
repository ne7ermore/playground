import numpy as np
import copy
import queue


class Sudoku(object):
    def __init__(self, board):
        board = np.asarray(board)
        assert board.shape == (9, 9)

        self.results = queue.Queue()
        valids = self.gather_value(board)

        copy_v = copy.deepcopy(valids)
        copy_b = board.copy()

        self.solve(copy_v, copy_b)

    def gather_value(self, board):
        nums = [i for i in range(1, 10)]
        valids = {(i, j): nums.copy() for i in range(9)
                  for j in range(9) if board[i, j] == 0}

        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v != 0:
                    for index in range(9):
                        if (i, index) in valids and v in valids[(i, index)]:
                            valids[(i, index)].remove(v)

                        if (index, j) in valids and v in valids[(index, j)]:
                            valids[(index, j)].remove(v)

                    _row, _col = i // 3, j // 3
                    for i_row in range(3):
                        for i_col in range(3):
                            _idx = (_row * 3 + i_row, _col * 3 + i_col)
                            if _idx in valids and v in valids[_idx]:
                                valids[_idx].remove(v)

        return valids

    def solve(self, valids, board):
        if len(valids) == 0:
            self.results.put([board])
            return

        slot = min(valids.keys(), key=lambda x: len(valids[x]))
        nums = valids[slot]
        for n in nums:
            r, c = slot
            copy_b = board.copy()
            copy_b[r, c] = n

            copy_v = copy.deepcopy(valids)
            del copy_v[slot]

            for index in range(9):
                if (index, c) in copy_v and n in copy_v[(index, c)]:
                    copy_v[(index, c)].remove(n)
                    if len(copy_v[(index, c)]) == 0:
                        return

                if (r, index) in copy_v and n in copy_v[(r, index)]:
                    copy_v[(r, index)].remove(n)
                    if len(copy_v[(r, index)]) == 0:
                        return

            _row, _col = r // 3, c // 3
            for i_row in range(3):
                for i_col in range(3):
                    _idx = (_row * 3 + i_row, _col * 3 + i_col)
                    if _idx in copy_v and n in copy_v[_idx]:
                        copy_v[_idx].remove(n)
                        if len(copy_v[_idx]) == 0:
                            return

            self.solve(copy_v, copy_b)


if __name__ == "__main__":
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    s = Sudoku(board)

    for r in s.results.get():
        print(r)

    '''
    [[5 3 4 6 7 8 9 1 2]
     [6 7 2 1 9 5 3 4 8]
     [1 9 8 3 4 2 5 6 7]
     [8 5 9 7 6 1 4 2 3]
     [4 2 6 8 5 3 7 9 1]
     [7 1 3 9 2 4 8 5 6]
     [9 6 1 5 3 7 2 8 4]
     [2 8 7 4 1 9 6 3 5]
     [3 4 5 2 8 6 1 7 9]]
    '''
