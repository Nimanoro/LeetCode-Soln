# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for _ in range(n + 1):
            if first is None:
                return head  
            first = first.next
        
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next

        return dummy.next
if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = s.removeNthFromEnd(head, 2)
    while result:
        print(result.val)
        result = result.next
