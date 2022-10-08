# Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
n,s=int(input("Enter a decimal number to print its binary equivalent: ")),""
while(n>0):
    s=str(int(n%2))+s
    n=int(n/2)
print("Binary Equivalent of a given decimal number is : ",s)