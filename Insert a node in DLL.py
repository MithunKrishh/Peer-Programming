class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def insertBeforeHead(self, head, X):
        newNode = Node(X)
        
        if head is None:
            return newNode
        
        newNode.next = head
        head.prev = newNode
        return newNode