class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length()!= t.length()) {
            return false;
        }

        HashMap<Character, Integer> hc = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            hc.put(c, hc.getOrDefault(c, 0) + 1);
        }
        for (int j = 0; j < t.length(); j++) {
            char c = t.charAt(j);
            if (hc.containsKey(c)) {
                int count = hc.get(c) - 1;
                if (count == 0) {
                    hc.remove(c);
                } else {
                    hc.put(c, count);
                }
            } else {
                return false;
            }
        }
        return hc.isEmpty();
    }
}