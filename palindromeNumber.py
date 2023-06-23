class Solution(object):
    def isPalindrome(self, x):
        front = []
        back = []

        num = str(x)
        for i in range(len(num)):
            front.append(num[i])

        for i in range(len(num)-1, -1, -1):
            back.append(num[i])
        
        if front == back:
            return True
        else:
            return False

sol = Solution()
print(sol.isPalindrome(152))

# prints reverse of a string
str = "pratik"
print(str[::-1])