#A) Definded as a function F as Fn=Fn-1+Fn-2. Write a Python program which accepts a value for N (where N>0) as input and pass this value to the functin.
#Display suitable error message if the condition for input value is not followed.


#Functin for nth Fibonacci number

def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
        #First Fibonacci number is 0
    elif n==1:
        return 0
    #Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
#Driver Program
num=int(input("Enter the number"))
print('fibonacci is',Fibonacci(num))
