class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Calculate the frequency of each element
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        // Use a min-heap to keep track of the top K frequent elements
        PriorityQueue<Map.Entry<Integer, Integer>> heap = new PriorityQueue<>(
            (a, b) -> a.getValue() - b.getValue()
        );

        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            heap.offer(entry);
            if (heap.size() > k) {
                heap.poll();
            }
        }

        // Extract the elements from the heap into the result array
        int[] elements = new int[k];
        int index = 0;
        while (!heap.isEmpty()) {
            elements[index++] = heap.poll().getKey();
        }

        return elements;
    }
}