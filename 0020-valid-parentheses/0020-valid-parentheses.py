class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        parenthesis = {')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char in parenthesis:
                if st and st[-1] == parenthesis[char]:
                    st.pop()
                else:
                    return False
            else:
                st.append(char)

        return len(st) == 0