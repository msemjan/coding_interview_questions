from math import floor

class Solution: 
    def getRange(self, arr, target):
        idx = self.binSearch(arr, 0, len(arr)-1, target)

        if idx is None:
            print("Idx is None")
            return -1

        if idx == -1:
            return -1

        left_idx = idx
        right_idx = idx
        
        while(right_idx + 1 < len(arr) and arr[right_idx + 1] == target):
            right_idx += 1
        
        while(left_idx - 1 >= 0 and arr[left_idx - 1] == target):
            left_idx -= 1

        return (left_idx, right_idx)

    def binSearch(self, arr, left_idx, right_idx, target):
        #print(arr," ",left_idx," ",right_idx," ",target)

        if right_idx < left_idx or left_idx < 0 or len(arr) <= right_idx :
            return -1
        
        if right_idx == left_idx:
            if arr[right_idx] == target:
                print(right_idx)
                return right_idx
            else:
                return -1

        mid_idx = floor((left_idx+right_idx)/2)

        if arr[mid_idx] == target:
            print(mid_idx)
            return mid_idx

        if target < arr[mid_idx]:
            idx = self.binSearch(arr, left_idx, mid_idx - 1, target)
        else:
            idx = self.binSearch(arr, mid_idx + 1, right_idx, target)

        if idx != -1:
            print(idx)
            return idx
        else:
            return -1
  
# Test program 
#arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
#x = 2
#print(Solution().getRange(arr, x))
# [1, 4]
#arr = [1,3,3,5,7,8,9,9,9,15]
#x = 9
#print(Solution().getRange(arr, x))
# [6, 8]

#arr = [100, 150, 150, 153]
#x = 150
#print(Solution().getRange(arr, x))
# [1, 2]

arr = [0,9,9,9,9,10]
x = 9
print(Solution().getRange(arr, x))
# [-1, -1]
