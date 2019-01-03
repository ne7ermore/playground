class SegmentTreeNode:
    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value
        self.left = self.right = None


class SegmentTree:
    def __init__(self, arr, fn):
        self.fn = fn
        self.arr = arr
        self.root = self.builder(0, len(arr)-1)

    def builder(self, left, right):
        if left > right:
            return None

        if left == right:
            return SegmentTreeNode(left, right, self.arr[left])

        mid = (left+right) // 2
        node = SegmentTreeNode(left, right, self.fn(self.arr[left:right+1]))
        node.left = self.builder(left, mid)
        node.right = self.builder(mid+1, right)

        return node

    def query(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.value

        vs = []
        mid = (node.start+node.end)//2

        if mid >= start:
            vs.append(self.query(node.left, start, end))

        if mid + 1 <= end:
            vs.append(self.query(node.right, start, end))

        return self.fn(vs)

    def modify(self, node, index, value):
        if node.start == node.end == index:
            node.value = value
            return

        mid = (node.start+node.end)//2
        if index <= mid:
            self.modify(node.left, index, value)
        else:
            self.modify(node.right, index, value)

        node.value = self.fn([node.left.value, node.right.value])


if __name__ == "__main__":
    arr = [3, 5, 2, 7, 4, 2, 11, 9]
    st = SegmentTree(arr, max)

    assert st.query(st.root, 0, 5) == 7

    st.modify(st.root, 1, 100)
    st.modify(st.root, 7, 1000)

    assert st.query(st.root, 0, 5) == 100
