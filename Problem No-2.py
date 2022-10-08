# Write a python script to calculate sum of squares of first N natural numbers.
n=int(input("Enter the value of n to print the sum of squares of first n natural numbers : "))
i,sum=1,0
while(i<=n):
    sum=(i*i)+sum
    i=i+1
print("Sum of squares : ",sum )
print()