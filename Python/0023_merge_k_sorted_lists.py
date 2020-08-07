class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        def merge2Lists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
        left, right = 0, len(lists) - 1
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = merge2Lists(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]

if __name__ == '__main__':
    s = Solution()
    L1 = ListNode(1)
    L1.next = ListNode(4)
    L1.next.next = ListNode(5)
    L2 = ListNode(1)
    L2.next = ListNode(3)
    L2.next.next = ListNode(4)
    L3 = ListNode(2)
    L3.next = ListNode(6)
    
    inputLists = [L1, L2, L3]

    outputLists = s.mergeKLists(inputLists)

    while outputLists:
        print(outputLists.val)
        outputLists = outputLists.next