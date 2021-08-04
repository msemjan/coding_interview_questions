'''
# Edit Distance (AirBnB)
Given two strings, determine the edit distance between them. The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution) needed to change one string to the other.

For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).
'''

def distance(s1, s2):
    # Matrix of Levenshtein distances
    d = [[0 for _ in range(len(s1))] for _ in range(len(s2))]

    for k in range(len(s1)):
        d[0][k] = k

    for k in range(len(s2)):
        d[k][0] = k

    for l in range(len(s1)):
        for k in range(len(s2)):
            if s1[l] == s2[k]:
                substitutionCost = 0
            else:
                substitutionCost = 1

            d[k][l] = min(d[k-1][l] + 1,                    # deletion
                          d[k][l-1] + 1,                    # insertion
                          d[k-1][l-1] + substitutionCost    # substitution
                         )
    return d[-1][-1]

print(distance('biting', 'sitting'))
# 2



