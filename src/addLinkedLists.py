from math import floor

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        one = l1
        two = l2
        sumList = None
        current = None
        remainder = 0

        while True:
            if (one is not None) and (two is not None):
                if sumList is None:
                    sumList = ListNode(0)
                    current = sumList
                else:
                    current.next = ListNode(0)
                    current = current.next

                current.val = floor((one.val + two.val + remainder)%10)
                remainder =  floor((one.val + two.val + remainder)/10)
                one = one.next
                two = two.next
            elif one is not None:
                if sumList is None:
                    sumList = ListNode(0)
                    current = sumList
                else:
                    current.next = ListNode(0)
                    current = current.next

                current.val = floor((one.val + remainder)%10)
                remainder =  floor((one.val + remainder)/10)
                one = one.next
            elif two is not None:
                if sumList is None:
                    sumList = ListNode(0)
                    current = sumList
                else:
                    current.next = ListNode(0)
                    current = current.next

                current.val = floor((two.val + remainder)%10)
                remainder =  floor((two.val + remainder)/10)
                two = two.next
            else:
                if remainder!=0:
                    current.next = ListNode(remainder)
                break
        return sumList

l1 = None #ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(2)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val,end=" ")
    result = result.next
# 7 0 8
print()

