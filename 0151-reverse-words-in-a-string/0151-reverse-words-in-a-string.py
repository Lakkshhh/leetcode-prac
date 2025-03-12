class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        ans=[]
        for i in reversed(words):
            if i:
                ans.append(i)
        return ' '.join(ans)