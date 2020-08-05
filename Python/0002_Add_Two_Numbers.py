
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            if l1 and not l2:
                val = l1.val + carry
            if not l1 and l2:
                val = l2.val + carry
            if l1 and l2:
                val = l1.val + l2.val + carry
            carry = val // 10
            current.next = ListNode(val % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    s = Solution()
    node = s.addTwoNumbers(l1, l2)
    while node:
        print(node.val)
        node = node.next

