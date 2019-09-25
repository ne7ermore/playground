class Solution {
public:
    int strStr(string haystack, string needle) {
        int lh = haystack.length();
        int ln = needle.length();
        if (!ln) return 0;
        
        vector<int> tmp(ln, 0);
        for (int i = 1, len = 0; i < ln; i++) {
            len = tmp[i-1];
            while(len && needle[len] != needle[i])
                len = tmp[len-1];
            tmp[i] = len+(needle[len] == needle[i]);
        }
        
        int i = 0, len = 0;
        while (i < lh) {
            while (len && needle[len] != haystack[i]) len = tmp[len-1];
            if (needle[len] == haystack[i]) {
                if (len == ln-1) return i - len;
                len++;
            }
            i++;
        }
        return -1;
    }
};