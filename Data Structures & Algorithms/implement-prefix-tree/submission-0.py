class PrefixNode:
    def __init__(self):
        self.map = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.map:
                curr.map[c] = PrefixNode()
            curr = curr.map[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.map:
                return False
            curr = curr.map[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.map:
                return False
            curr = curr.map[c]
        return True
        