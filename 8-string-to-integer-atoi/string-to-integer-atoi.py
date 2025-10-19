class Solution(object):
    def myAtoi(self, s):
        INT_MAX = 2**31-1
        INT_MIN = -2**31

        result = ''
        reading = False
        sign = 1
        for i in s:
            if i == ' ' and not reading:
                continue
            elif i in ('+','-') and not reading:
                sign = 1 if i == '+' else -1
                reading = True
            elif i in ('+','-') and reading:
                break
            elif i.isdigit():
                reading = True
                result += i
            elif reading and not i.isdigit():
                break
            else:
                return 0
        
        if not result:
            return 0
        result = int(result)*sign
        return max(min(result, INT_MAX), INT_MIN)