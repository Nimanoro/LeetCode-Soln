# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head):
        stack = []
        m = head
        while m != None:
            stack.append(m.val)
            m = m.next
        m = head
        while m != None:
            m.val = stack.pop()
            m = m.next
        return head
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    Solution.reverseList(None ,head)
    while head != None:
        print(head.val)
        head = head.next
    
    head = ListNode(1)
    head.next = ListNode(2)
    Solution.reverseList(None ,head)
    while head != None:
        print(head.val)
        head = head.next
        