class Solution(object):
    def isMatch(self, s, p):
        # Initialize memoization dictionary to store (i, p_index) results
        memo = {}
        
        def match(i, p_index):
            # Check if state (i, p_index) is already computed
            if (i, p_index) in memo:
                return memo[(i, p_index)]
            
            # Base case: both s and p are exhausted
            if i == len(s) and p_index == len(p):
                return True
            
            # Base case: p is exhausted, s is not
            if p_index == len(p):
                return False
            
            # Base case: s is exhausted, p is not
            # If next character in p is '*', try zero repetition
            if i == len(s):
                if p_index + 1 < len(p) and p[p_index + 1] == '*':
                    return match(i, p_index + 2)
                return False
            
            # Check for '*' in p (two-character check)
            if p_index + 1 < len(p) and p[p_index + 1] == '*':
                # Zero repetition: skip the character and '*' in p
                if match(i, p_index + 2):
                    memo[(i, p_index)] = True
                    return True
                # One repetition: consume one character from s, keep '*' in p
                if (p[p_index] == s[i] or p[p_index] == '.') and 97 <= ord(s[i]) <= 122:
                    if match(i + 1, p_index):
                        memo[(i, p_index)] = True
                        return True
                memo[(i, p_index)] = False
                return False
            
            # Normal match: consume one character from both s and p
            if p[p_index] == s[i] or (p[p_index] == '.' and 97 <= ord(s[i]) <= 122):
                result = match(i + 1, p_index + 1)
                memo[(i, p_index)] = result
                return result
            
            # No match
            memo[(i, p_index)] = False
            return False
        
        # Start matching from the beginning of s and p
        return match(0, 0)