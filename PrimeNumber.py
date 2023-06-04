# Write a Python program to print the prime numbers for a user provided range
lower = int(input('Enter The Lower Range'))
upper = int(input('Enter The Upper Range'))
for n in range(lower, upper):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)