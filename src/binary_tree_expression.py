# -*- coding: utf-8 -*-
"""
Arithmetic Binary Tree (Apple)

You are given a binary tree representation of an arithmetic expression. 
In this tree, each leaf is an integer value,, and a non-leaf node is one of 
the four operations: '+', '-', '*', or '/'.

Write a function that takes this tree and evaluates the expression.

Example:

    *
   / \
  +    +
 / \  / \
3  2  4  5


This is a representation of the expression (3 + 2) * (4 + 5), and should return
45.


Created on Sat Nov  9 21:12:34 2019

@author: ms
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if type(self.val) == int:
            return str(self.val)
        return "(" + str(self.left) + " " + str(self.val) + " " + str(self.right) + ")"
        
PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    if type(root) is not Node:
        return None
    
    return eval(str(root))

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
# 45