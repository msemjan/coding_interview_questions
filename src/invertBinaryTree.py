'''
# Invert a Binary tree (Twitter)
You are given the root of a binary tree. Invert the binary tree in place. That is, all left children should become right children, and all right children should become left children.
Example:

    a
   / \
  b   c
 / \  /
d   e f

The inverted version of this tree is as follows:

  a
 / \
 c  b
 \  / \
  f e  d

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def preorder(self):
        s = str(self.value)
        if self.left is not None: 
            s+= self.left.preorder()
        if self.right is not None: 
            s+= self.right.preorder()
        return s

def invert(node):
    node.left, node.right = node.right, node.left
    if node.left is not None:
        invert(node.left)
    if node.right is not None:
        invert(node.right)

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

print(root.preorder())
# a b d e c f 
invert(root)
print(root.preorder())
# a c f b e d
