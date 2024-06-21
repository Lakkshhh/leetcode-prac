class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set valid = new HashSet();
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                char current = board[i][j];
                if(current != '.') {
                    if(!valid.add(current + " at row " + i) ||
                       !valid.add(current + " at column " + j) ||
                       !valid.add(current + " at sub-box " + i/3 + "-" + j/3)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}