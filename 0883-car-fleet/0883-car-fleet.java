class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        float[] times = new float[target + 1];
        for (int i = 0; i < position.length; i++) {
            times[position[i]] = (float)(target - position[i]) / (float)speed[i];
        }

        float previous = 0;
        int fleetCount = 0;
        for (int i = times.length - 1; i >= 0; i--) {
            if (times[i] > previous) {
                previous = times[i];
                fleetCount++;
            }
        }

        return fleetCount;
    }
}

// class Solution {
//     public int carFleet(int target, int[] position, int[] speed) {
//         int[][] combo = new int[position.length][2];
//         Stack<Double> fleets = new Stack();

//         for(int i = 0; i < position.length; i++) {
//             combo[i][0] = position[i];
//             combo[i][1] = speed[i];
//         }

//         Arrays.sort(combo, Comparator.comparingInt(o -> o[0]));

//         for(int i = combo.length - 1; i >= 0; i--) {
//             double time = (double) (target - combo[i][0]) / combo[i][1];

//             if(!fleets.isEmpty() && time <= fleets.peek()) {
//                 continue;
//             }
//             fleets.push(time);
//         }
//         return fleets.size();
//     }
// }