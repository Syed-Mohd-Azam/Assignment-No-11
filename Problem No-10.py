# Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method).
n,s=int(input("Enter a decimal number to print the octal equivalent of a given decimal number: ")),""
while(n>=8):
    s=str(int(n%8))+s
    n=int(n/8)
s=str(n)+s
print("Octal equivalent of given binary number: ",s)