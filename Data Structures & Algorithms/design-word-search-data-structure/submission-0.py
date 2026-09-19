class DictNode:
    def __init__(self):
        self.map = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = DictNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.map:
                curr.map[c] = DictNode()
            curr = curr.map[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def recur(i, curr):
            if i == len(word):
                return curr.end
            
            if word[i] == ".":
                for c in curr.map:
                    if recur(i+1, curr.map[c]):
                        return True
            else:
                if word[i] not in curr.map:
                    return False
                curr = curr.map[word[i]]
                if recur(i+1, curr):
                    return True
            return False
        return recur(0, self.root)