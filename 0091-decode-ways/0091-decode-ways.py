class Solution:
    def numDecodings(self, s: str) -> int:
        # memo[i] = number of ways to decode the substring starting at index i
        #
        # There is exactly 1 way to decode an empty string, so we start
        # with the base case: index len(s) has 1 decoding.
        memo = {len(s): 1}

        def dfs(i):
            # If we've already calculated the number of decodings
            # starting at index i, return the saved result.
            if i in memo:
                return memo[i]

            # A number starting with 0 cannot be decoded.
            # For example, "06" is invalid.
            if s[i] == "0":
                return 0

            # Option 1: Decode the current digit by itself.
            # Then move to the next character.
            res = dfs(i + 1)

            # Option 2: Decode the current digit together with the
            # next digit as a two-digit number.
            #
            # Valid two-digit numbers are:
            #   10-19  -> starts with "1"
            #   20-26  -> starts with "2" and second digit is 0-6
            #
            # We also make sure i + 1 is still inside the string.
            if (
                (i + 1) < len(s)
                and (
                    s[i] == "1"
                    or (s[i] == "2" and s[i + 1] in "0123456")
                )
            ):
                # If the two digits form a valid number, decode them
                # together and move forward by 2 positions.
                res += dfs(i + 2)

            # Save the result so we don't have to recalculate it later.
            memo[i] = res

            return res

        # Start decoding from the first character.
        return dfs(0)


        # full code straight up lol
        # memo = { len(s) : 1 }

        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if s[i] == "0":
        #         return 0
            
        #     res = dfs(i + 1)
        #     if (i + 1) < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
        #         res += dfs(i + 2)
            
        #     memo[i] = res
        #     return res
        
        # return dfs(0)