class Solution {
    public String reverseWords(String s) {
        String ans = new String();
        String cleaned = s.trim();
        int len = cleaned.length();
        int i = 0;

        while(i < len) {
            while(cleaned.charAt(i) == ' ') {
                i++;
            }

            int j = i + 1;
            while(j < len && cleaned.charAt(j) != ' ') {
                j++;
            }

            String word = cleaned.substring(i, j);
            if(ans.isEmpty()) {
                ans = word;
            }
            else {
                ans = word + " " + ans;
            }

            i = j+1;
        }
        return ans;
    }
}