class Solution(object):
    def intToRoman(self, num):
        thousands = ['','M','MM','MMM']
        hunderds = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']

        return (thousands[num//1000] + hunderds[(num%1000)//100] + tens[(num%100)//10] + ones[num%10])