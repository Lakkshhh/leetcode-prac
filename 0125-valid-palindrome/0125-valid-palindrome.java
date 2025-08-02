class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder cleaned = new StringBuilder();

        for(char i: s.toCharArray()) {
            if(Character.isLetterOrDigit(i)) {
                cleaned.append(Character.toLowerCase(i));
            }
        }

        int left = 0;
        int right = cleaned.length() - 1;

        while(left < right) {
            if(cleaned.charAt(left) != cleaned.charAt(right)) {
                return false;
            }
                left++;
                right--;
        }
        return true;
    }
}