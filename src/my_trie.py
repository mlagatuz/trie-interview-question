class TrieNode():

    def __init__(self):
        self.children = [None] * 26
        self.is_word_end = False

class Trie():
    
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def insert(self, key):
        node = self.root
        key_length = len(key)
        for level in range(key_length):
            index = ord(key[level]) - ord('a')
            if not node.children[index]:
                node.children[index] = self.getNode()
            node = node.children[index]
        node.is_word_end = True

    def search(self, key):
        node = self.root
        key_length = len(key)
        for level in range(key_length):
            index = ord(key[level]) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.is_word_end