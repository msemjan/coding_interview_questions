import functools

def word_search(matrix, word):
    '''
    You are given a 2D array of characters, and a target string. Return whether
    or not the word target word exists in the matrix. Unlike a standard word 
    search, the word must be either going left-to-right, or top-to-bottom in 
    the matrix.
    '''
    sumMtx = ['' for i in range(len(matrix[0]))]

    for k in range(len(matrix)):
        sumMtx = [sumMtx[l] + matrix[k][l] for l in range(len(matrix[0]))]
        if functools.reduce(lambda x, y: x + y, matrix[k],'').find(word) >= 0:
            return True

    for k in range(len(sumMtx)):
        if sumMtx[k].find(word) >= 0:
            return True

    return False

matrix = [
          ['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']
         ]

print(word_search(matrix, 'IPBS'))
# True
