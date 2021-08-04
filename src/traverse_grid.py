# -*- coding: utf-8 -*-
"""
# Ways to Traverse a Grid (Microsoft)

You 2 integers n and m representing an n by m grid, determine the number of 
ways you can get from the top-left to the bottom-right of the matrix y going 
only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.

@author: ms
"""

def num_ways(n, m):
    grid = [[0 for _ in range(n)] for _ in range(m)]
    
    for k in range(m):
        for l in range(n):
            if (k == 0 and l == 0):
                grid[k][l] = 0
            elif l - 1 < 0 and k - 1 >= 0:
                grid[k][l] = min(grid[k][0], grid[k-1][l]) + 1
            elif l - 1 >= 0 and k - 1 < 0:
                grid[k][l] = min(grid[k][l], grid[0][l]) + 1
            else:
                grid[k][l] = min(grid[k][l-1], grid[k-1][l]) + 1
    
    for k in range(m):
        for l in range(n):
            print(grid[k][l], end=" ")
        print()
    
    return grid[m-1][n-1]

print(num_ways(4, 4))
# 2