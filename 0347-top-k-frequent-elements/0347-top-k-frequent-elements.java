class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int freq : nums) {
            map.put(freq, map.getOrDefault(freq, 0) + 1);
        }
        
        List<Integer> ls = new ArrayList<>(map.keySet());
        Collections.sort(ls, (a, b) -> map.get(b) - map.get(a));
        int[] result = new int[k];
        int index = 0;
        
        for(int i = 0; i<k; i++) {
            result[index] = ls.get(i);
            index++;
        }
        return result;
    }
}
