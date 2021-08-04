def merge(self, list1, list2):
    # Fill this
    one = list1
    two = list2

# Definition for a Linked List.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = str(x)
        if self.next != None:
            s += " " + self.next.str()
        return s
