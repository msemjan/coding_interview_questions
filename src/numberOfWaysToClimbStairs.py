'''
# Number of Ways to Climb Stairs (Linkedln)
You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

Can you find a solution in O(n) time?
'''
def staircase(n):
    # Solved using dynamic programming. 
    arr_n = [1 for i in range(n)]
    for i in range(n):
        staircaseSolver(i+1, arr_n)
    return arr_n[-1]

def staircaseSolver(n, arr_n):
    if n == 2:
        arr_n[n-1] = 2
        return
    if n > 2:
        arr_n[n-1] = arr_n[n-2] + arr_n[n-3]

print(staircase(4))
# 5
print(staircase(5))
# 8
