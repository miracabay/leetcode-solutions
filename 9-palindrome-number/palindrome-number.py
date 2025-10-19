class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        num = str(x)
        left = 0
        right = len(num)-1

        while right > left:
            if num[left] != num[right]:
                return False
            left += 1
            right -= 1

        return True