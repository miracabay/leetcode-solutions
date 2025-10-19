class Solution(object):
    def longestPalindrome(self, s):
        max_pal = ""
        
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(max_pal):
                    max_pal = s[left:right+1]
                left -= 1
                right += 1
            
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(max_pal):
                    max_pal = s[left:right+1]
                left -= 1
                right += 1
                
        return max_pal