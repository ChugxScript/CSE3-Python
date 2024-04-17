# Write a PYTHON program to print the natural numbers up to n
def print_natural_numbers():
    n = int(input("Enter n: "))
    print("Natural numbers up to", n, "are:")

    if n <= 0:
        print(n, " don't have natural numbers.")
    else:
        for i in range(1, n+1):
            print(i)
# print_natural_numbers()


# Write a PYTHON program to print even numbers up to n
def print_even_numbers():
    n = int(input("Enter n: "))

    if n < 0:
        print(n, " don't have even numbers.")
    else:
        print("Even numbers up to", n, "are:")
        for i in range(0, n+1, 2):
            print(i)
# print_even_numbers()


# Write a PYTHON program to print odd numbers up to n
def print_odd_numbers():
    n = int(input("Enter n: "))

    if n <= 0:
        print(n, " don't have odd numbers.")
    else:
        print("Odd numbers up to", n, "are:")
        for i in range(1, n+1, 2):
            print(i)
# print_odd_numbers()


# Write a PYTHON program that prints (1 2 4 8 16 32 … n^2)
def print_sequence_a():
    n = int(input("Enter n: "))

    if n < 1:
        print("n must start at 1")
    else:
        print("The sequence is:")
        for i in range(n):
            print(2 ** i)
# print_sequence_a()

def print_sequence_b():
    n = int(input("Enter n: "))

    total = 0
    factorial = 1
    for i in range(n + 1):
        if i != 0:
            factorial *= i
        total += 1 / factorial

    print("\nThe sum of the sequence up to", n, "terms is:", total)
# print_sequence_b()

