class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count1 = {}
        # count2 = {}

        # for char in s:
        #     count1.update({char : count1.get(char, 0) + 1})

        # for char in t:
        #     count2.update({char : count2.get(char, 0) + 1})
        
        # return count1 == count2
        return sorted(list(t)) == sorted(list(s))