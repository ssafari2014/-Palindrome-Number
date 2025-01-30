class Solution:
    def isPalindrome(self, x):
        x1 = str(x)
        y = x1[::-1]
        if y == str(x):
            return True
        else:
            return False


x = ""
Output =  Solution()
Output.isPalindrome(x)
