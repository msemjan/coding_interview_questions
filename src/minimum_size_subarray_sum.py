# -*- coding: utf-8 -*-
"""
Minimum Size Subarray Sum (Amazon)

Given an array of n positive integers and a positive integer s, find the 
minimal length of a contiguous subarray of which the sum ≥ s. If there isn't 
one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2

Explanation: the subarray [4,3] has the minimal length under the problem 
constraint.


@author: ms
"""

class Solution:
    def minSubArrayLen(self, arr, x):
        n = len(arr)
        
        # Initialize current sum and minimum length 
        curr_sum = 0
        min_len = n + 1
      
        # Initialize starting and ending indexes 
        start = 0
        end = 0
        while (end < n): 
          
            # Keep adding array elements while current 
            # sum is smaller than x 
            while (curr_sum <= x and end < n): 
                curr_sum += arr[end] 
                end += 1
      
            # If current sum becomes greater than x. 
            while (curr_sum >= x and start < n): 
              
                # Update minimum length if needed 
                if (end - start < min_len): 
                    min_len = end - start  
                    #print(arr[start:end])
      
                # remove starting elements 
                curr_sum -= arr[start] 
                start += 1
          
        return min_len  
            

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
