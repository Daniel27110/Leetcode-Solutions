class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([i for i in s if i.isalnum()])
        return all(s[i] == s[~i] for i in range(len(s) // 2))
