Time complexity​: O(n)

1. Initialize a variable to keep track of the maximum area of water.
2.  Initialize a pointer low at the beginning of the array.
3.  Initialize another pointer high at the end of the array.
4.  Continue looping until left pointer is not equal to or exceeds the right pointer.
5.  We use Math.max to update "max" to be the maximum of its current value and current_area. This ensures that "max" always holds the maximum area encountered so far.
6.  Calculate the area of the container formed by the two lines at indices low and high. It is the width of the container (distance between the two pointers) multiplied by the minimum of the heights of the two lines.
7.  If the height of the line at the low pointer is less than the height of the line at the high pointer, increment the low pointer. This means we're trying to find a line with greater height to potentially increase the area.
8.  Otherwise, decrement the high pointer. This means we're trying to find a line with greater height on the right side to potentially increase the area.
9.  After the loop ends, return the maximum area calculated.
