class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> res = new LinkedList<>();
        int max = 0;
        for(int candy : candies) {
            max = Math.max(max, candy);
        }
        for(int i = 0; i < candies.length; i++) {
            if(candies[i] + extraCandies >= max) {
                res.add(true);
            } else {
                res.add(false);
            }
        }
        return res;
    }
}