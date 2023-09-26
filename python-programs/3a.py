s = input("Enter a sentence: ")
w, d, u, l = 0, 0, 0, 0
word = s.split()
w = len(word)
for c in s:
    if c.isdigit():
        d = d + 1

    elif c.isupper():
        u = u + 1

    elif c.islower():
        l = l + 1

print ("No of Words: ", w)
print ("No of Digits: ", d)
print ("No of Uppercase letters: ", u)
print ("No of Lowercase letters: ", l)
