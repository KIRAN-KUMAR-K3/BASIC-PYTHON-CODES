num= int(input("Enter a value : "))
temp= str(num)
if temp == temp[::-1]:
 print("Entered Value is Palindrome")
else:
 print("Entered Value is Not a Palindrome")
for i in range(10):
 if temp.count(str(i)) > 0:
     print(str(i), "appears", temp.count(str(i)), "times")