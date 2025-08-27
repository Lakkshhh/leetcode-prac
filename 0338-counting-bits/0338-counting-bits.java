class Solution {
    public int[] countBits(int n) {
        int res[] = new int[n + 1];
        int place = 0;
        ArrayList<String> ans = new ArrayList<String>();
        for(int i = 0; i <= n; i++) {
            ans.add(Integer.toBinaryString(i));
        }

        for(String c: ans) {
            int len = 0;

            while(len < c.length()) {
                if(c.charAt(len) == '1') {
                    res[place] += 1;
                }
                len++;
            }
            place++;
        }
        return res;
    }
}