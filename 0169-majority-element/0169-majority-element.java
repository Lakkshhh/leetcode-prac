class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> countMap = new HashMap<>();
        int n = nums.length;

        for(int num: nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
            if(countMap.get(num) > n/2) {
                return num;
            }
        }
        return -1;
    }
}

// import java.util.Arrays;

// class Solution {
//     public int majorityElement(int[] nums) {
//         Arrays.sort(nums);
//         return nums[nums.length / 2];
//     }
// }