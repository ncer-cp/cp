# Display prime numbers from 1 to 100
print("Prime numbers from 1 to 100 are:")
for num in range(2, 101):  # 1 is not prime
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

print("\n")

# Check if a given number is prime
n = int(input("Enter a number to check if it's prime: "))
if n <= 1:
    print("Not a Prime Number")
else:
    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
