from collections import deque


class BkTree(object):
    def __init__(self, distance_fn):
        self.dfn = distance_fn
        self.root = None

    def add(self, item):
        node = self.root
        if node is None:
            node = (item, {})
            return

        while True:
            p, children = node
            d = self.dfn(item, p)
            if d in children:
                node = children[d]
            else:
                children[d] = (item, {})
                break

    def search(self, item, n):
        if self.root is None:
            return []

        q = deque([self.root])
        res = []
        while q:
            p, children = q.pop()
            d = self.dfn(item, p)
            if d <= n:
                res.append((p, d))

            for dist, c in children.items():
                if d-n <= dist <= d+n:
                    q.append(c)

        res.sort(key=lambda x: x[1])
        return res
