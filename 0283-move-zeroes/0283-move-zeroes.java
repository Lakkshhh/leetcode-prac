class Solution {
    public void moveZeroes(int[] nums) {
        int left = 0;
        int right = 1;
        for(int i = 0; i < nums.length - 1; i++) {
            if(nums[left] == 0 && nums[right] != 0) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right++;
            } else if(nums[left] == 0 && nums[right] == 0) {
                right++;
            } else {
                left++;
                right++;
            }
        }
    }
}