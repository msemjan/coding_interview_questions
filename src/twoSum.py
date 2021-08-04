def two_sum(l, k):
    # Fill this in.
    s = set()

    for ii in range(len(l)):
        if (k - l[ii]) in s:
            return True
        else:
            s.add(l[ii])

    return False

print(two_sum([4,7,1,-3,2], 5))
# True


print(two_sum([1, 0], 5))
# False

print(two_sum([5, 0], 5))
# True

print(two_sum([0, 5], 5))
# True

print(two_sum([], 5))
# ??
