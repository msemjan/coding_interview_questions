'''
# Create simple calculator (Google)
Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. Assume the expression is properly formed.

Example:
> Input: - ( 3 + ( 2 - 1 ) )
> 
> Output: -4
'''
def eval(expression):
    pass

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left  = None

    def evalTree(self):
        ans = 0

        return ans
    
    def __str__(self):
        s = ''
        if self.right:
            s += str(self.right) + ' '
        s += self.value
        if self.left:
            s += ' ' + str(self.left)

def treeFromStr(s):
    '''
    Creates a binary tree from a string that is in-order.
    '''
    

print(eval('- (3 + ( 2 - 1 ) )'))
# -4


