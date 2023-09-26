m1=int(input("Enter the marks of the first test: "))
m2=int(input("Enter the marks of the second test: "))
m3=int(input("Enter the marks of the third test: "))

maximum=min(m1,m2,m3)  # Find the maximum test score
s2=m1+m2+m3-maximum  # Sum of two highest test scores
avg=s2/2  # Calculate the average of the two highest scores
print("The best of two average test marks is:", avg)