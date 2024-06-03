class Solution {
    public int[] productExceptSelf(int[] nums) {
        int N = nums.length;
        
        int[] left_nums = new int[N];
        int[] right_nums = new int[N];
        int[] ans = new int[N];
        
        left_nums[0] = 1;
        right_nums[N-1] = 1;
        
        for(int i = 1; i <= N-1; i++) {
            left_nums[i] = left_nums[i-1]*nums[i-1];
        }
        
        for(int i = N-2; i >= 0; i--) {
            right_nums[i] = right_nums[i+1]*nums[i+1];
        }
        
        for(int i = 0; i<N; i++) {
            ans[i] = left_nums[i]*right_nums[i];
        }
        return ans;
    }
}