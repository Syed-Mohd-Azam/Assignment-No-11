# Write a python script to calculate sum of digits of a given number.
n=int(input("Enter a number to calculate the sum of digits : "))
sum=0
while (n>0):
    sum=sum+int(n%10)
    n=n/10
print("Sum of digits : ",sum)