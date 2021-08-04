class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverseIteratively(self, head):
        # Implement this.
        prev_node = None
        this_node = self
        next_node = self.next

        while next_node is not None:
            this_node.next = prev_node
            prev_node = this_node
            this_node = next_node
            next_node = next_node.next

        this_node.next = prev_node
        prev_node = this_node
        
        return prev_node

    # Recursive Solution      
    def reverseRecursively(self, head):
        # Implement this.
        if self.next is not None:
            self.next.reverseRecursively(self)
        self.next = head
    

# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
#end = testHead.reverseIteratively(testHead)
testHead.reverseRecursively(None)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4

some_node = ListNode(0)
some_node.next = ListNode(1)
some_node.next.next = ListNode(2)
some_node.next.next.next = ListNode(3)
some_node.next.next.next.next = ListNode(4)
end = some_node.reverseIteratively(some_node)
end.printList()
