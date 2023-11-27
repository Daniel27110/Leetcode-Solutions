from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        string = ""
        while head:
            string += str(head.val)
            head = head.next
        return string == string[::-1]
