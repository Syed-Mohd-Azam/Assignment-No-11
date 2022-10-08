# Write a python script to calculate sum of first N natural numbers.
n=int(input("Enter the value of n  to print sum of first n natural numbers : "))
i,sum=1,0
while (i<=n):
    sum=sum+i
    i=i+1
print()
print("Sum of first ",n," natural numbers is : ",sum)
print()