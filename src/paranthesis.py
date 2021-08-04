class Solution:
    def isValid(self, s):
        stack = list()
        for i in range(len(s)):
            if s[i] is '(':
                stack.append(s[i])
            elif s[i] is '[':
                stack.append(s[i])
            elif s[i] is '{':
                stack.append(s[i])
            elif s[i] is ')':
                ch = stack.pop()
                if ch is not '(':
                    return False
            elif s[i] is ']':
                ch = stack.pop()
                if ch is not '[':
                    return False
            elif s[i] is '}':
                ch = stack.pop()
                if ch is not '{':
                    return False
            else:
                continue
        if len(stack)!=0:
            return False

        return True


# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
