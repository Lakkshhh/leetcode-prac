class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length()!= t.length()) return false;
        int[] char_count = new int[26];
        for(char ch : s.toCharArray()) {
            char_count[ch-'a']++;
        }
        for(char ch : t.toCharArray()) {
            char_count[ch-'a']--;
        }
        for(int count : char_count) {
            if(count!=0) return false;
        }
        return true;
    }
}
