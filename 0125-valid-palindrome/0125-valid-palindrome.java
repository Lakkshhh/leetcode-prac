class Solution {
    public boolean isPalindrome(String s) {
        if (s.isEmpty()) {
        	return true;
        }
        int start = 0;
        int last = s.length() - 1;
        while(start <= last) {
        	char currFirst = s.charAt(start);
        	char currLast = s.charAt(last);
        	if (!Character.isLetterOrDigit(currFirst )) {
        		start++;
        	} else if(!Character.isLetterOrDigit(currLast)) {
        		last--;
        	} else {
        		if (Character.toLowerCase(currFirst) != Character.toLowerCase(currLast)) {
        			return false;
        		}
        		start++;
        		last--;
        	}
        }
        return true;
    }
}


// class Solution {
//     public boolean isPalindrome(String s) {
//         String fixed_string = "";
//         for(char c : s.toCharArray()) {
//             if(Character.isDigit(c) || Character.isLetter(c)) {
//                 fixed_string += c;
//             }
//         }
//         fixed_string = fixed_string.toLowerCase();
        
//         int a_pointer = 0;
//         int b_pointer = fixed_string.length() - 1;
        
//         while(a_pointer <= b_pointer) {
//             if(fixed_string.charAt(a_pointer) != fixed_string.charAt(b_pointer)) {
//                 return false;
//             }
//             a_pointer += 1;
//             b_pointer -= 1;
//         }
//         return true;
//     }
// }
