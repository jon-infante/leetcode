# Merge two sorted linked lists and return it as a sorted list. 
# The list should be made by splicing together the nodes of the first two lists.
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    @staticmethod
    def return_ll(node: ListNode) -> List:
        lis = []
        while node:
            lis.append(node.val)
            node = node.next
        return lis

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return []
        if l1 == None: return l2
        if l2 == None: return l1

        head = ListNode()
        o = head
        curr1 = l1
        curr2 = l2
        while curr1 and curr2:
            if curr1 is None:
                o.next = ListNode(curr2.val)
                o = o.next
                curr2 = curr2.next
            if curr2 is None:
                o.next = ListNode(curr1.val)
                o = o.next
                curr1 = curr1.next

            if curr1.val < curr2.val:
                node1 = ListNode(curr1.val)
                if o.val:
                    o.next = node1
                    o = o.next
                else:
                    o = node1
                curr1 = curr1.next
            elif curr2.val < curr1.val:
                node2 = ListNode(curr2.val)
                if o.val:
                    o.next = node2
                    o = o.next
                else:
                    o = node2
                curr2 = curr2.next
            
            else: #equal
                if o.val is None:
                    o.val = curr1
                else:
                    o.next = ListNode(curr1)
                    o = o.next
                o.next = ListNode(curr2)
                o = o.next
                curr1 = curr1.next
                curr2 = curr2.next

                
        return self.return_ll(head)




if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(2, ListNode(3, ListNode(4)))
    # [1,2,2,3,4,4]
    solution = Solution()
    print(solution.mergeTwoLists(l1,l2))
    pass      

