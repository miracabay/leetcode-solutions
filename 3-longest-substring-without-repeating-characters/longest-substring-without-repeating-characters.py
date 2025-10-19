class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0

        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            max_length = max(max_length, len(seen))

        return max_length