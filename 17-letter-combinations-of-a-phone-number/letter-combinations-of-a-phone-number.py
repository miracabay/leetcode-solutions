from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        char_set = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        letters = [char_set[d] for d in digits]

        return [''.join(p) for p in product(*letters)]