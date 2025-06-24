# Function to find all divisors of a number
def find_divisors(n):
    print(f"Divisors of {n} are:", end=" ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()

# Function to find GCD using Euclidean Algorithm
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Divisors
find_divisors(num1)
find_divisors(num2)

# GCD
gcd = find_gcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {gcd}")
