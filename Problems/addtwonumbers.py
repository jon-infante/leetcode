# Definition for singly-linked list.
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in 
# reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tot_sum = 0
        def traverse_sum(self, ll, pointer=0, sum=0):
            #Taken our given position in the linked list, we add a number of trailing zeros to indicate an increase in its place value
            while True:
                zeros = pointer * '0'
                sum += int(f'{ll.val}{zeros}')
                ll = ll.next
                if not ll:
                    return sum
                pointer += 1
        #Gather the reversed total
        if l1:
            tot_sum += traverse_sum(self,l1)
        if l2:
            tot_sum += traverse_sum(self,l2)

        output = str(tot_sum)[::-1]
        l3 = ListNode(None)

        #Attach each node to the linked list
        def linked_sum(self, stri_num ,ll):
            cur = ll
            for i, num in enumerate(stri_num):
                cur.val = int(num)
                if i == len(stri_num)-1:
                    break
                cur.next = ListNode()
                cur = cur.next
                
            return ll

        output_node = linked_sum(self,output,l3)

        return output_node



# code for l1
# sum += 2 * 1(amount of 0s[0]) (0 0s)
# sum += 4 * 10(one zero) 
# sum += 3 * 100(two zeros)
# sum = 342
# repeat for l2
# sum += (5*1) + (6*10) + (4*100)
# sum = 807
# turn the int into something iterable, like a string
# output = str(sum)
# output_node.val = output[len(output)-1]
# output_node.next = ListNode(output[1],ListNode(output[0]))


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    l3 = ListNode(3)
    l4 = ListNode(5)
    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))
