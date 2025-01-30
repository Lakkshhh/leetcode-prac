class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        maxString = min(len(str1), len(str2))
        result = 0
        for i in range(1, maxString+1):
            if len(str1)%i == 0 and len(str2)%i == 0:
                result = i
        if (str1+str2) == (str2+str1):
            return str(str1[:result])
        else:
            return ""