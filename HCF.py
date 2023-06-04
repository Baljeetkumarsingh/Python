# This is python script to find hcf of 2 number
"""
This script allow you to find hcf of 2 number
usage:
Enter the first number : 12
Enter the second number : 20
HCF of 12 and 20 is : 
Thank You!
"""


def hcf():
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))

    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if ((a % i == 0) and (b % i == 0)):
            hcf = i
    print("HCF of" a "and" b "is : " hcf)


hcf()
