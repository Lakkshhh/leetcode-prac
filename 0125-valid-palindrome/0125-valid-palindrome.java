class Solution {
    public boolean isPalindrome(String s) {
        ArrayList<Character> cleanString = new ArrayList<>();

        for(char i: s.toCharArray()) {
            if(Character.isLetterOrDigit(i)) {
                i = Character.toLowerCase(i);
                cleanString.add(i);
            }
        }

        int left = 0;
        int right = cleanString.size() - 1;

        while(left < right) {
            if(cleanString.get(left).equals(cleanString.get(right))) {
                left++;
                right--;
            }
            else {
                return false;
            }
        }
        return true;
    }
}