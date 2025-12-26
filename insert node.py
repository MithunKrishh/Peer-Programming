class Solution:
    def insertAtHead(self, head, X):
        newNode = ListNode(X)
        newNode.next = head
        return newNode
