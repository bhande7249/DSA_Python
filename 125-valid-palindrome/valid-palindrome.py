class Solution:
    def isPalindrome(self, s: str) -> bool:
        a= "".join(list(map(lambda x: x.lower(),filter(lambda x:x.isalnum() ,s))))
        i=0
        j=len(a)-1
        return a==a[::-1]
