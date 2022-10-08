# Write a python script to calculate factorial of a given number.
from re import I

# Write a python script to calculate factorial of a given number.
print()
n=int(input("Enter the number to calculate factorial : "))
i,fact=1,1
while(i<=n):
    fact=fact*i 
    i=i+1
print("Factorial is : ",fact)
print()