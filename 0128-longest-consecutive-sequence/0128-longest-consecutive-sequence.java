class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> num_set = new HashSet();
        for(int num : nums) {
            num_set.add(num);
        }
        
        int max_sequence_length = 0;
        for(int i = 0; i < nums.length; i++) {
            int current_num = nums[i];
            int current_sequence_length = 1;
            if(!num_set.contains(current_num-1)) {
                while(num_set.contains(current_num+1)) {
                    current_num += 1;
                    current_sequence_length += 1;
                }
            }
            max_sequence_length = Math.max(max_sequence_length, current_sequence_length);
        }
        return max_sequence_length;
    }
}