class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> output_arr = new ArrayList<String>();
        backtrack(output_arr, "", 0, 0, n);
        return output_arr;
    }
    
    public void backtrack(List<String> output_arr, String s, int open, int close, int n) {
        if (s.length() == n * 2) {
            output_arr.add(s);
            return;
        }
        
        if (open < n) {
            backtrack(output_arr, s + "(", open + 1, close, n);
        }
        
        if (close < open) {
            backtrack(output_arr, s + ")", open, close + 1, n);
        }
    }
	// See above tree diagram with parameters (left, right, s) for better understanding
}