# -*- coding: utf-8 -*-
"""
# Create a simple calculator (Google)
Given a mathematical expression with just single digits, plus signs, negative 
signs, and brackets, evaluate the expression. Assume the expression is properly
formed.

Example:
Input: - ( 3 + ( 2 - 1 ) )
Output: -4

@author: ms
"""

import re

class Tree:
    def __init__(self, value, left, right):
        self.value = value
        self.left  = left
        self.right = right
    
    def __str__(self):
        l_str = "" if self.left is None else "(" + str(self.left) + ")"
        r_str = "" if self.right is None else "(" + str(self.right) + ")"
        
        return l_str + str(self.value) + r_str
    
    def eval(self):
        l_val = 0 if self.left is None else self.left.eval()
        r_val = 0 if self.right is None else self.right.eval()
        return l_val + self.value + r_val
    
    @staticmethod
    def tree_from_str(self, s):        
        if s is None:
            return None
        
        if s.len() == 0:
            return None
        
        s.replace(" ", "")          
        
        it = re.finditer("[+\-*\/]", s)
        
        for match in it:
            left_str = s[0:match.span()[0]]
            left_str = left_str[1:] if left_str[0] == "(" else left_str
            left_str = left_str[:-1] if left_str[-1] == ")" else left_str
            
            right_str = s[match.span()[1]:-1]
            right_str = right_str[1:] if right_str[0] == "(" else right_str
            right_str = right_str[:-1] if right_str[-1] == ")" else right_str
            
            op = s[match.span()[0]]
            
            
            print("Left: ", left, " [Pos: ", op ," ]  Right: ", right)

from collections import deque

class Evaluator:
    def __init__(self, expression):
        self.expression = expression
        self.value = Evaluator.eval(self.expression)
        
    @staticmethod
    def eval(expression):
        """
        Evaluates mathematic expression using a stack based algorithm - the 
        Shunting-yard algorithm.
        """
        s = list()
        sp = expression.split(" ")
        
        for symbol in sp:
            if symbol.isnumberic():
                q.appendleft(symbol)
            elif symbol in ["+","-","*","/","^"]:
                s.append(symbol)
            

def eval(expression):
    t = Tree.tree_from_str(expression)
    return t.eval()

print(eval('- ( 3 + ( 2 - 1 ) )'))
# -4