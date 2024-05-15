Time Complexity: ​O(n * k * log(k)), where n is the number of strings in the input array strs and k is the maximum length of a string in the input array.

1) First, I initialize an empty unordered map which will store the groups of anagrams.
2) Iiterate through each word in the input string list strs.
3) I create a string variable called word and assign it the value of the current word.
4) Next, sort the characters in word using the sort() function.
5) After sorting, insert sortedWord as the key into the map, and we push the original word into the list associated with that key, basically as values. Since the sorted word is a unique sorted representation of all the anagrams, it serves as the key in the mp map, and the associated vector holds all the anagrams.
6) Iterate through each key-value pair in the map using a if loop to check if the sorted word already exists in the map. If it does, just add the current word to the ArrayList as a value to the unique sorted key. If it doesnt exisit, then put the sorted word as a new key with the current word as the value in the form of an ArrayList.
7) Finally, return the ArrayList containing all the values from the map, which contains the groups of anagrams.
