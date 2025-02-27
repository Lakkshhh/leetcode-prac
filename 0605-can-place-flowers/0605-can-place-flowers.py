class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                right_plot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if left_plot and right_plot:
                    flowerbed[i] = 1
                    ans += 1
        return ans >= n