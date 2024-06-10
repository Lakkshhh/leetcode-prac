class Solution {
    public boolean isValid(String s) {
        if(s.length() % 2 != 0) return false;
        
        Stack<Character> sc = new Stack<>();
        for(char c : s.toCharArray()) {
            if(c == '(' || c == '{' || c == '[') {
                sc.push(c);
            }
            else if(c == ')' && !sc.isEmpty() && sc.peek() == '(') {
                sc.pop();
            }
            else if(c == '}' && !sc.isEmpty() && sc.peek() == '{') {
                sc.pop();
            }
            else if(c == ']' && !sc.isEmpty() && sc.peek() == '[') {
                sc.pop();
            }
            else {
                return false;
            }
        }
        return sc.isEmpty();
    }
}