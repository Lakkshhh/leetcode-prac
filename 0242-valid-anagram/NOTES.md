Time complexity: O(n)
Space complexity: O(1)​

1) First, we check if the lengths of both strings are the same, since only the characters in the string are being jumbled and the length remains the same. If the length is found to be different, we can return false.
2) Then, we could use a HashMap which was my first approach but not the fastest and takes up a lot of up a lot of space. Hence, we will work with arrays.
3) An integer array char_count of size 26 is created. This array is used to store the frequency of each character in the input strings. Each index corresponds to a character, with index 0 representing 'a', index 1 representing 'b', and so on.
4) The loop iterates through each character of string s. For each character, it calculates its position in the array by subtracting the ASCII value of 'a' from the character's ASCII value. Then, it increments the count of that character in the freq array.
5) Similar to the previous loop, this loop iterates through each character of string t. For each character, it decrements the count of that character in the array.
6) After processing both strings, this loop checks if there are any non-zero values in the array. If any non-zero value is found, it means that the frequencies of characters in s and t are not the same, so the method returns false, indicating that s and t are not anagrams.
7) If all characters have the same frequency in both strings, the method returns true, indicating that s and t are indeed anagrams of each other.
