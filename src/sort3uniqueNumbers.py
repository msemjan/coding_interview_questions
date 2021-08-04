def sortNums(nums):
    uniques = 3
    counts = [0]*uniques

    for ii in range(len(nums)):
        counts[nums[ii]-1] += 1
    
    ordered = []
    for ii in range(uniques):
        [ordered.append(ii+1) for _ in range(counts[ii])]

    return ordered

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]

