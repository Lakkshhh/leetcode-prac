class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1+str2) == (str2+str1):
            maxString = gcd(len(str1), len(str2))
            return str(str1[:maxString])
        else:
            return ""