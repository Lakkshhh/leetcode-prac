Time Complexity: O(m.log(n)) - Binary search takes O(log N) iterations. If piles has m elements, each iteration involves a feasibility check which takes O(m) time.

1. 'left' is initialized to 1 because the minimum speed must be at least '1' banana per hour.
2. 'right' is initialized to 'Integer.MAX_VALUE' because this sets an upper bound on the possible eating speed.
