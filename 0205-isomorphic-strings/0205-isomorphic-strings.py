class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        indices_s = {}
        indices_t = {}

        for i in range(len(s)):
            if s[i] not in indices_s:
                indices_s[s[i]] = i

            if t[i] not in indices_t:
                indices_t[t[i]] = i

            if indices_s[s[i]] != indices_t[t[i]]:
                return False
        
        return True

        # char_map = {}

        # for sc, tc in zip(s, t):
        #     if sc in char_map:
        #         if char_map[sc] != tc:
        #             return False
        #     elif tc in char_map.values():
        #         return False

        #     char_map[sc] = tc

        # return True