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





// class Solution {        // Bucket solution to get Time Complexity: o(n)
//     public int[] topKFrequent(int[] nums, int k) {
//         List<Integer>[] bucket = new List[nums.length + 1];
//         HashMap<Integer, Integer> hm = new HashMap<>();
//         for (int num : nums) {
//             hm.put(num, hm.getOrDefault(num,0) + 1);
//         }
//         for (int key : hm.keySet()) {
//             int freq = hm.get(key);
//             if (bucket[freq] == null) {
//                 bucket[freq] = new ArrayList<>();
//             }
//             bucket[freq].add(key);
//         }
//         int[] ans = new int[k];
//         int pos = 0;
//         for (int i = bucket.length - 1; i >= 0; i--) {
//             if (bucket[i] != null) {
//                 for (int j = 0; j < bucket[i].size() && pos < k; j++) {
//                     ans[pos] = bucket[i].get(j);
//                     pos++;
//                 }
//             }
//         }
//         return ans;
//     }
// }
