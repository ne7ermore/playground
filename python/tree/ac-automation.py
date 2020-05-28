import collections


class TrieNode(object):

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.fail = None
        self.word = None


class AcAutomation(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            node = node.children[c]

        node.word = word

    def build_fail(self):
        queue = []
        for node in self.root.children.values():
            node.fail = self.root
            queue.append(node)

        while queue:
            node = queue.pop(0)

            for char, child_node in node.children.items():
                p = node.fail
                while True:
                    if p is None:
                        child_node.fail = self.root
                        break

                    if char in p.children:
                        child_node.fail = p.children[char]
                        break

                    p = p.fail

                queue.append(child_node)

    def search(self, word):
        node, ret, idx = self.root, [], 0

        while idx < len(word):
            char = word[idx]

            if char in node.children:
                node = node.children[char]
                if node.word:
                    ret.append((node.word, idx-len(node.word)+1))

                if node.fail and node.fail.word:
                    ret.append((node.fail.word, idx-len(node.fail.word)+1))

                idx += 1
            else:
                node = node.fail

                if node is None:
                    node = self.root
                    idx += 1

        return ret


if __name__ == "__main__":

    ac = AcAutomation()
    ac.add('abcdef')
    ac.add('abhab')
    ac.add('bcd')
    ac.add('cde')
    ac.add('cdfkcdf')

    ac.build_fail()

    print(ac.search('bcabcdebcedfabcdefababkabhabk'))
