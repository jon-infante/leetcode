# Definition for singly-linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tot_sum = 0
        def traverse_sum(self, ll, pointer=0, sum=0):
            #Taken our given position in the linked list, we add a number of trailing zeros to indicate an increase its place value
            while True:
                zeros = pointer * '0'
                sum += int(f'{ll.val}{zeros}')
                ll = ll.next
                #If the value is None
                if not ll:
                    return sum
                pointer += 1
        #Gather the reversed total
        if l1:
            tot_sum += traverse_sum(self,l1)
        if l2:
            tot_sum += traverse_sum(self,l2)

        output = str(tot_sum)[::-1]
        l3 = ListNode(0)
        def linked_sum(self, stri_num ,ll):
            if len(stri_num) == 1:
                return ListNode(int(stri_num))
            ll.val = int(stri_num[0])
            #Recursively add new nodes to the linked list
            ll.next = linked_sum(self,stri_num[1::], ll)
    
            return ll
            # for i, num in enumerate(stri_num):
            #     ll.val = stri_num[i-1]
            #     if i == len(stri_num):
            #         return ll
            #     ll.next = ListNode(0)

            #     ll = ll.next
                
            # return ll

        output_node = linked_sum(self,output,l3)
        return output_node.val





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
