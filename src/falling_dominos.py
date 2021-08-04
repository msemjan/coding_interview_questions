'''
Falling Dominos (Twitter)

Given a string with the initial condition of dominoes, where:
    . represents that the domino is standing still
    L represents that the domino is falling to the left side
    R represents that the domino is falling to the right side

Figure out the final position of the dominoes. If there are dominoes that 
get pushed on both ends, the force cancels out and that domino remains 
upright.

Example:
    Input:  ..R...L..R.
    Output: ..RR.LL..RR
'''

class Solution(object):
    def pushDominoes(self, dominoes):
        if len(dominoes) in [0, 1]:
            return dominoes
       
        l_dominoes = list(dominoes)
        k_dominoes = list(dominoes)

        change = True
        while change:
            change = False
            for ii in range(len(l_dominoes)):
                if l_dominoes[ii] in ['R','L']:
                    continue
                else:
                    # Getting neighbors
                    left, right = '.', '.'
                    
                    if 0<=ii-1:
                        left = l_dominoes[ii-1]
                    if ii+1 < len(l_dominoes):
                        right = l_dominoes[ii+1]
                   
                    # Update of the ii-th domino
                    if ((left, right) == ('R', 'L')) or ((left, right) == ('L', 'R')):
                        continue
                    elif left == 'R':
                        k_dominoes[ii] = 'R'
                        change = True
                    elif right == 'L':
                        k_dominoes[ii] = 'L'
                        change = True
            
            l_dominoes = k_dominoes
        return "".join(l_dominoes)

print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR
