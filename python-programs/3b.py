str1 = input("Enter First String:\n")
str2 = input("Enter Second String\n")

if len(str2) < len(str1):
    st2 = len(str2)
    st1 = len(str1)
else:
    st2 = len(str1)
    st1 = len(str2)
match= 0
for i in range(st2):
    if str1[i] == str2[i]:
        match += 1


print("Similarity between two said String:")
print(match/ st1*100)
