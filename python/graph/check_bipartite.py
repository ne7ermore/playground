def check_bipartite(adj_list):

    V = len(adj_list)

    set_type = [-1 for v in range(V)]
    set_type[0] = 0

    q = [0]

    while q:
        v = q.pop(0)

        if adj_list[v][v]:
            return False

        for u in range(V):
            if adj_list[v][u]:
                if set_type[u] == set_type[v]:
                    return False
                elif set_type[u] == -1:
                    set_type[u] = 1 - set_type[v]
                    q.append(u)

    return True


if __name__ == "__main__":
    adj_list = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0]]

    assert check_bipartite(adj_list)
