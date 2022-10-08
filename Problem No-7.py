# Write a python script to count digits in a given number.
n=int(input("Enter a number to count the no of digits : "))
count=0
if n==0:
    count=1
else :
    while(n>0):
        n=int(n/10)
        count=count+1
print()
print("No of digits : ",count)
print()