def fibonacci(n):
    a = 0
    b = 1
    print ("fibonacci series:")
    while a <= n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()    

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("factorial of ", n, "is:", fact)

def main():
    n = int(input("enter any number :"))
    fibonacci(n)
    factorial(n)

main()