class Solution {
    public int trap(int[] height) {
        if(height.length == 0) return 0;
        int res = 0;
        int left = 0;
        int right = height.length-1;
        int lMax = height[left];
        int rMax = height[right];
        while(left < right){
            if(lMax < rMax){
                left++;
                lMax = Math.max(lMax, height[left]);
                res += lMax - height[left];
            }else{
                right--;
                rMax = Math.max(rMax, height[right]);
                res += rMax - height[right];
            }
        }
        return res;
    }
}