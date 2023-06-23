#cheack wheather the given number is palondrome are not?!
number=int(input ("Enter the number: 10"))
temp=number
reverse=0        
while(number>0):
    dig=number%10
    reverse=reverse*10+dig
    number=number//10
    print("The reverse number is:",reverse)
    if temp==reverse:
        print("the number is a palidrome")
    else:
        print("The nubmer is not palidrom")