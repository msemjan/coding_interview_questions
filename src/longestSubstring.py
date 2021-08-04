class Solution:
    def lengthOfLongestSubstring(self, s):
        '''
        Finds the length of the longest substring of s.
        '''
        if s is None:
            return 0

        used = set()
        counter = 0
        maxLen  = 0

        for i in range(len(s)):
            if s[i] not in used:
                counter += 1
                used.add(s[i])
            else:
                used = set()
                used.add(s[i])
                if counter > maxLen:
                    maxLen = counter
                counter = 1

        return max(maxLen, counter)



print(Solution().lengthOfLongestSubstring(None))                  # 0
print(Solution().lengthOfLongestSubstring(''))                    # 0
print(Solution().lengthOfLongestSubstring('abcd'))                # 4
print(Solution().lengthOfLongestSubstring('aaaa'))                # 1
print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')) # 10
