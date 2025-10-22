class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new="".join([char.lower() for char in s if char.isalnum()])
        reverted_s_new=s_new[::-1]
        return s_new == reverted_s_new
    
        
        