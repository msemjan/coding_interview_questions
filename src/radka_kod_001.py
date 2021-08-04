# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:45:03 2019

@author: ms
"""

def getBonuses(performance):
    # None list
    if performance is None:
        return None
    
    # empty list
    if len(performance)==0:
        return []

    # one element 
    if len(performance)==1:
        return [1]
    
    # more than one element
    bonuses = [1 for _ in range(len(performance))]
    
    # bonus for the first and the last
    if performance[0] > performance[1]:
        bonuses[0] += 1
        
    if performance[-1] > performance[-2]:
        bonuses[-1] += 1
    
    # bonuses for those in the middle
    for i in range(len(performance)-2):
        if performance[i+1] > performance[i+2]:
            bonuses[i+1] += 1
        
        if performance[i+1] > performance[i]:
            bonuses[i+1] += 1

    return bonuses

print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]