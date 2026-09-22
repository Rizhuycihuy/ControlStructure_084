n = int(input("Enter n: "))

a = 0
b = 1

print("Fibonacci series:")
while a <= n:
    print(a, end=" ")

    a, b = b, a + b