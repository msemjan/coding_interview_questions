# TODO - doesn't work yet
# Merge K Sorted Linked Lists (Twitter)
# You are given an array of k sorted singly linked lists. 
# Merge the linked lists into a single sorted linked list and return it.
#

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def merge(lists):
    sorted_list = None
    head = None
    if lists is None or lists == None:
        return sorted_list
    
    while any([i is None for i in lists]):
        # Find the node with the smallest value
        min_val = float('inf')
        min_idx  = -1
        for i in range(len(lists)):
            if lists[i] is not None and lists[i].val < min_val:
                min_val = lists[i].val
                min_idx  = i

        # Add the node to merged list
        if head is None:
            sorted_list = Node(min_val)
            head = sorted_list
        else:
            head.next = Node(min_val)
            head = head.next

        if lists[i] is not None:
            lists[i] = lists[i].next
        print(str(sorted_list), [str(i) for i in lists], "\n")
    return sorted_list

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print merge([a, b])
# 123456
