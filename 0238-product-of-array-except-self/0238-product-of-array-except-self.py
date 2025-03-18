class Solution:
    # def prod(self, n, nums):
    #     product = 1
    #     for i in range(len(nums)):
    #         if i != n: 
    #             product = product * nums[i]
    #     return product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans=[]
        # for i in range(len(nums)):
        #     mul = self.prod(i, nums)
        #     ans.append(mul)

        # return ans
        n=len(nums)
        ans, pre, suf = [0] * n, [0] * n, [0] * n
        pre[0] = 1
        suf[n-1] = 1

        for i in range(1, n):
            pre[i] = pre[i-1]*nums[i-1]

        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1]*nums[i+1]

        for i in range(n):
            ans[i] = pre[i]*suf[i]

        return ans
