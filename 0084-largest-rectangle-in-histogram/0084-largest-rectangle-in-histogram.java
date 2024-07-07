class Solution {
    public int largestRectangleArea(int[] heights) {
        int maxArea = 0;
        Stack<Pair> stack = new Stack<>();
        int n= heights.length;
        for (int i = 0; i <= n; i++) {
            int start = i;
            // Pop elements from stack while the current height is less than the height at stack's top
            while (!stack.isEmpty() && (i==n || stack.peek().height > heights[i])) {
                Pair pair = stack.pop();
                int index = pair.index;
                int height = pair.height;
                int length =i-index;
                maxArea = Math.max(maxArea, height * length);
                start = index;  // Update start to the index of the popped element
            }
            if(i<n) stack.push(new Pair(start, heights[i]));  // Push current index and height as a pair
        }

        return maxArea;
    }
    class Pair {
        int index;
        int height;

        Pair(int index, int height) {
            this.index = index;
            this.height = height;
        }
    }
}