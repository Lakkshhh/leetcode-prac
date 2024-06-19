Time complexity: O(n)

Approach:
I will first check if the concatenated strings str1 + str2 are equal to str2 + str1. If they are not equal, there is no common GCD substring, so I'll return an empty string. If they are equal, I will calculate the GCD of the lengths of str1 and str2 using a recursive function. The GCD value will represent the length of the common GCD substring. I'll return the substring of str1 from index 0 to the calculated GCD value.​
