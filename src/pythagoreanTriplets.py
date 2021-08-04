'''
# Find Pythagorean Triplets (Uber)

Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

Example:
> Input: [3, 5, 12, 5, 13]
> 
> Output: True

Here, 5^2 + 12^2 = 13^2.
'''

def findPythagoreanTriplets(nums):
    nums_sq = [i for i in (map(lambda x: x**2, nums))]
    
    for k in range(0, len(nums_sq) - 2):
        for l in range(k + 1, len(nums_sq) - 1):
            if nums_sq[k] + nums_sq[l] in nums_sq:
                return True

    return False

print(findPythagoreanTriplets([3, 12, 5, 13]))
# True

print(findPythagoreanTriplets([1, 1, 27]))
# False

