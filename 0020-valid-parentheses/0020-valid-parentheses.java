class Solution {
    public boolean isValid(String s) {
        Stack<Character> sc = new Stack<>();
        
        for(char ch : s.toCharArray()) {
            if(ch=='(' || ch=='[' || ch=='{') {
                sc.push(ch);
            }
            else {
                if (sc.isEmpty()) {
                    return false;
                }
                char top = sc.peek();
                if((ch==')' && top=='(') || (ch==']' && top=='[') || (ch=='}' && top=='{')) {
                    sc.pop();
                }
                else {
                    return false;
                }
            }
        }
        return sc.isEmpty();
    }
}