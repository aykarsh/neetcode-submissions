class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=s.replace(" ","")
        s=''
        for i in a:
            if i.isalnum():
                s+=i.lower()
            else:
                pass
        print(s)
        print(s[0::],s[::-1])
        if s[0::]==s[::-1]:
            return True
        else:
            return False