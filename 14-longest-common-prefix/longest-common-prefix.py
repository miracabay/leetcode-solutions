class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return result

        result = ''
        min_str = min(strs, key=len)
        min_len = len(min_str)
        strs.remove(min_str)

        if not strs:
            return min_str

        for j in range(min_len):
            char = min_str[j]
            for word in strs:
                if word[j] != char:
                    return result
            result += char
        
        return result