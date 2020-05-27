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
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            p = None

            for char, child_node in node.children.items():
                if node == self.root:
                    child_node.fail = self.root

                else:
                    p = node.fail
                    while p is not None:
                        if char in p.children:
                            child_node.fail = p.fail
                            break
                        p = p.fail

                    if p is None:
                        child_node.fail = self.root

                queue.append(child_node)

    def search(self, word):
        node, ret, idx = self.root, [], 0

        while idx < len(word):
            char = word[idx]

            if char in node.children:
                node = node.children[char]
                if node.word is not None:
                    ret.append((node.word, idx-len(node.word)+1))

                if node.fail and node.fail.word is not None:
                    ret.append((node.fail.word, idx-len(node.fail.word)+1))

                idx += 1
            else:
                p = node.fail
                if p is not None and p != self.root:
                    p = p.fail
                    break

                node = self.root
                idx += 1

        return ret


if __name__ == "__main__":

    ac = AcAutomation()
    ac.add('he')
    ac.add('she')

    ac.build_fail()
    print(ac.root.children['s'].children['h'].children['e'].fail)
    print(ac.root.children['h'].children['e'])
    print(ac.search('she'))
