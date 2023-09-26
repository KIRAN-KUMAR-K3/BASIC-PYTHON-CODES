class palindemo:
    def checkPalindrome(self, x):
        t = x
        v = 0
        while t>0:
            r = t%10
            v = r + (v*10)
            t = int(t/10)
        if v==x:
            return 1
print("Enter a Number: ", end="")
n = int(input())
obj1 = palindemo()
chk = obj1.checkPalindrome(n)
if chk==1:
    print("\nThe Given number Is Palindrome Number")
else:
    print("\nThe Given Number Is Not a Palindrome Number")
class palindemo1(palindemo):
    def checkPalindrome(self,str):
        mid = int(len(str) / 2)
        for i in range(0, mid):
            if str[i] != str[len(str) - i - 1]:
                return False
            return True

print("Enter a String: ", end="")
str = input().lower()
obj2 = palindemo1()
ch1=obj2.checkPalindrome(str)
if ch1==1:
    print("\nThe Given String Is a Palindrome String")
else:
    print("\nThe Given String Is Not a Palindrome String")