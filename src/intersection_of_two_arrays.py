# -*- coding: utf-8 -*-
"""
Given two arrays, write a function to compute their intersection (Amazon)

Given two arrays, write a function to compute their intersection - the 
intersection means the numbers that are in both arrays.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.

Created on Sat Nov  9 21:34:19 2019

@author: ms
"""

class Solution:
    def intersection(self, nums1, nums2):
        bigger_one = set()
        smaller_one = set()
        smaller_list = list()
        
        if len(nums1) < len(nums2):
            bigger_one = set(nums2)
            smaller_one = set(nums1)
            smaller_list = nums1
        else:
            bigger_one = set(nums1)
            smaller_one = set(nums2)
            smaller_list = nums2

        for e in smaller_list:
            if e not in bigger_one:
                smaller_one.remove(e)
                
        return list(smaller_one)
        
#        n1 = set(nums1)
#        n2 = set(nums2)       
#        return list(n1.intersection(n2))
        
    def printIntersection(self, arr1, arr2): 
        arr1.sort()
        arr2.sort()
        
        ans = []
        i,j = 0,0
        while i < len(arr1) and j < len(arr2): 
            if arr1[i] < arr2[j]: 
                i += 1
            elif arr2[j] < arr1[i]: 
                j+= 1
            else: 
                ans.append(arr2[j]) 
                j += 1
                i += 1
        return ans

print(Solution().printIntersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]
