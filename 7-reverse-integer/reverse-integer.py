class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        arr = str(x)
        negative = False
        if arr[0] == '-':
            negative = True
            arr = arr [1:]
        
        result = int(''.join(reversed(arr)))
        if result > INT_MAX:
            return 0
        return result*-1 if negative else result