class Solution {
    public void moveZeroes(int[] nums) {
        int lastZero = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != 0) {
                int temp = nums[lastZero];
                nums[lastZero] = nums[i];
                nums[i] = temp;
                lastZero++;
            }
        }
    }
}