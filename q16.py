# Write a program to print the factorial of a number accepted by the user.


n=int(input("Enter the number:"))
i=1
while n>0:
    i=i*n
    n=n-1
    print(i)
    i+=1