# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.tList = []
        
        while head:
            self.tList.append(head.val)
            head = head.next
            
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.tList)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()