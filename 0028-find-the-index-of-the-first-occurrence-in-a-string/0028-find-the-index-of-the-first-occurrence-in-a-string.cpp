class Solution {
public:
    int strStr(string mainn, string sub) {
        for (int p=0;p<mainn.length();p++) {
            if (mainn[p]==sub[0]){
                int i1=p+1;
                int j=1;
                while(mainn[i1] && sub[j]) {
                    if (mainn[i1]!=sub[j]) 
                        break;
                    i1++;
                    j++;
                }
                if (j==sub.length()) 
                    return p;
            }
        }
        return -1; 
    }
};