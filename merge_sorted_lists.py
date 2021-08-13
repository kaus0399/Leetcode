class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final_answer = answer = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                answer.next = l1
                l1 = l1.next
            else:
                answer.next = l2
                l2 = l2.next
            answer = answer.next
        answer.next = l1 or l2 
        return final_answer.next

'''Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.'''