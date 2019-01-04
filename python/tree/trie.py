import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return False

        return node.is_word
