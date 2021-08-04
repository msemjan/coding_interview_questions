'''
Reverse Integer (Linkedln)

Write a function that reverses the digits a 32-bit signed integer, x. Assume
that the enviroment can only integers withing the 32-signed integer range, [-2^31, 2^31-1]. The function returns 0 when the reversed integer overflows.

Example:
    Input:  123
    Output: 321
'''

class Solution:
    def reverse(self, x):
        '''
        Reverses the integer.
        '''
        ans = 0
        while x > 0:
            ans = 10*ans + x%10
            x = int(x/10)
        
        if -2**31 <= ans <= 2**31-1:
            return ans
        else:
            return 0

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
