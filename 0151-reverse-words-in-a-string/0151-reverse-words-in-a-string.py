class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(' ')
        ans=[]
        for i in reversed(words):
            if not i:
                continue
            else:
                ans.append(i)
        return ' '.join(ans)