class Solution {
    public boolean isSubsequence(String s, String t) {
        int x = 0;
        for(int i = 0; i < t.length(); i++) {
            if (s.isEmpty() || t.isEmpty()) {
                return true;
            }
            else if (x!=s.length() && t.charAt(i) == s.charAt(x)) {
                x++;
            }
        }
        if(x == s.length()) {
            return true;
        }
        else {
            return false;
        }
    }
}