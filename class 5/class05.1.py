#3 A). wirte a pyton program that accepts a sentence and find  the number of words, digits, uppercase letters and lowercase letters.
s=input("Enter a sentence:")
w, d, u, l=0,0,0,0
l_w=s.split()
w=len(l_w)
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isupper():
       l = l+1

    print("No of Words:",w)
    print("No of Digits:",d)
    print("No of uppercase letters:",u)
    print("No of Lowercase letters:",l)