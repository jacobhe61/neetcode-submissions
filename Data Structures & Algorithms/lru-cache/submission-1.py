class ListNode():
    def __init__(self, key=-1, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.hash = {}
        self.size = 0
        self.cap = capacity

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1

        self.hash[key].prev.next = self.hash[key].next
        self.hash[key].next.prev = self.hash[key].prev

        self.hash[key].prev = self.tail.prev
        self.hash[key].next = self.tail

        self.tail.prev.next = self.hash[key]
        self.tail.prev = self.hash[key]

        return self.hash[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            self.hash[key] = ListNode(key, value, self.tail, self.tail.prev)

            self.tail.prev.next = self.hash[key]
            self.tail.prev = self.hash[key]

            if self.size < self.cap:
                self.size += 1
            else:
                self.hash.pop(self.head.next.key)
                self.head.next.next.prev = self.head
                self.head.next = self.head.next.next

        else:
            self.hash[key].val = value
        
            self.hash[key].prev.next = self.hash[key].next
            self.hash[key].next.prev = self.hash[key].prev

            self.hash[key].prev = self.tail.prev
            self.hash[key].next = self.tail

            self.tail.prev.next = self.hash[key]
            self.tail.prev = self.hash[key]

        return