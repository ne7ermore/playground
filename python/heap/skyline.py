class Solution:
    def getSkyline(self, buildings):
        que, live = [0], []
        skyline = []
        pre = 0
        for l, r, h in buildings:
            live.append((l, -h))
            live.append((r, h))

        live.sort(key=lambda x: (x[0], x[1]))

        while live:
            res = live.pop(0)
            if res[1] < 0:
                que.append(-res[1])
                que.sort()
            else:
                que.pop(que.index(res[1]))

            cur = que[-1]
            if cur != pre:
                skyline.append([res[0], cur])
                pre = cur

        return skyline
