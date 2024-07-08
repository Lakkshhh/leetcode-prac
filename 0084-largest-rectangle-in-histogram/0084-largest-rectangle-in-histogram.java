class Solution {
    public int largestRectangleArea(int[] h) {
        int n = h.length;
        int maxArea = 0;
        Stack<Integer> st = new Stack();

        for(int i = 0; i <= n; i++) {
            int currHeight = i==n ? 0 : h[i];

            while(!st.isEmpty() && currHeight < h[st.peek()]) {
                int top = st.pop();
                int width = st.isEmpty() ? i : i-st.peek()-1;
                int area = h[top]*width;
                maxArea = Math.max(maxArea, area);
            }
            st.push(i);
        }
        return maxArea;
    }
}