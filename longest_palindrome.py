class Solution:
    def longestPalindrome_BF(self, s: str) -> str:
        #Bruteforce O(n^3) complextiy
        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        elif s == s[::-1]:
            return s
        else:
            longest_palindrome = None
            max_len = None
            for i in range(len(s)):
                for j in range(i+1,len(s)+1):
                    string = s[i:j]
                    if string == string[::-1]:
                        if longest_palindrome == None:
                            longest_palindrome = string
                            max_len = len(string)
                        else:
                            if len(string) > max_len:
                                longest_palindrome = string
                                max_len = len(string)    
            return longest_palindrome
       

    def longestPalindrome_DP(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        elif s == s[::-1]:
            return s
        else:
            n = len(s)
            DP = [[None for i in range(n)] for y in range(n)]
            for i in range(n-1):
                DP[i][i] = 1
            max_len = 1
            start = 0
            for l in range(2,n + 1):
                for i in range(n-l + 1):
                    end = i + l
                    if l == 2:
                        if s[i] == s[end - 1]:
                            DP[i][end-1] = 1
                            max_len = l
                            start = i
                    else:
                        if s[i] == s[end-1] and DP[i+1][end-2]:
                            DP[i][end-1]=1  
                            max_len = l
                            start = i
        return s[start:start+max_len]

          
if __name__ == '__main__':
    print(Solution().longestPalindrome_DP("angqzrtyuvwlkpornmjdgfybazabriktyucvbqwrkilyhgtrdfvenfovuyejwoqqkllpqrhfkvpzhxnvmhkmloprmbgfrsuwnrkgodyxhnekwodjfntke"))