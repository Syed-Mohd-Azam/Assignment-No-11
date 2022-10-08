# Write a python script to calculate sum of first N even natural numbers.
n=int(input("Enter the value of n to calculate the first n even natural numbers : "))
i,sum=1,0
while(i<=n):
    sum=sum+(2*i)
    i=i+1
print("Sum is : ",sum)
print()
