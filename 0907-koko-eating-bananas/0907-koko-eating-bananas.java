class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = Integer.MAX_VALUE;
        
        while(left < right){
            int mid = left + (right - left) / 2;
            if(canEatInTime(piles, mid, h)) right = mid;
            else left = mid + 1;
        }
        return left;
    }

    public boolean canEatInTime(int[] piles, int k, int h) {
        int hours = 0;
        for (int pile : piles) {
            hours += (pile + k - 1) / k;
            if (hours > h) return false; // Early exit if hours exceed h
        }
        return hours <= h;
    }
}
