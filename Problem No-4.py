# Write a python script to calculate sum of first N odd natural numbers.
n=int(input("Enter the value of n to calculate the sum of first n odd natural numbers : "))
i,sum=0,0
while(i<n):
    sum=(2*i+1)+sum
    i=i+1
print("Sum is : ",sum)
print()