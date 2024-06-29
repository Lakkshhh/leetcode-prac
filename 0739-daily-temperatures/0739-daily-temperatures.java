class Solution {
    public int[] dailyTemperatures(int[] temps) {
        Stack<Integer> index = new Stack<>();
        int[] res = new int[temps.length];
        for(int i = 0; i < temps.length; i++) {
            while(!index.isEmpty() && temps[index.peek()] < temps[i]) {
                int topIndex = index.pop();
                res[topIndex] = i - topIndex;
            }
            index.push(i);
        }

        return res;
    }
}