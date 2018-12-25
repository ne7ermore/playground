import heapq


def get_skyline(lrh):
    que, live = [0], []
    skyline = []
    for l, r, h in lrh:
        heapq.heappush(live, (l, -h))
        heapq.heappush(live, (r, h))

    while live:
        res = heapq.heappop(live)
        if res[1] < 0:
            if res[1] < que[0]:
                skyline.append([res[0], -res[1]])

            heapq.heappush(que, res[1])

        else:
            if -res[1] == que[0]:
                heapq.heappop(que)
                skyline.append([res[0], -que[0]])
            else:
                que.remove(-res[1])

    return skyline


if __name__ == "__main__":
    lrh = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    assert get_skyline(lrh) == [[2, 10], [3, 15], [7, 12], [
        12, 0], [15, 10], [20, 8], [24, 0]]
