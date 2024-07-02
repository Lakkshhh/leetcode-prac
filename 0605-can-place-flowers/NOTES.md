Time Complexity: O(n)

1. Check if n is 0: If n is 0, return true immediately because no new flowers need to be planted.
2. Iterate through each plot in the flowerbed: Loop from the beginning to the end of the flowerbed array.
3. Check if the current plot can have a flower:
4.   The current plot (flowerbed[i]) is empty (0).
5.   The previous plot (flowerbed[i-1]) is empty or it’s the first plot (i == 0).
6.   The next plot (flowerbed[i+1]) is empty or it’s the last plot (i == flowerbed.length - 1).
7. Plant a flower if the above conditions are met.
8. Plant a flower at the current plot (flowerbed[i] = 1).
9. Decrement n by 1.
10. If n becomes 0, return true because all flowers have been planted.
11. If the loop completes and n is not 0, return false because it was not possible to plant all n flowers.
