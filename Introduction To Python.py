print("Hello world")
a = eval(input("Enter first number:\n"))
b = eval(input("Enter Second number:\n"))

def fib(First,Second):
    fib = 0
    print(f"Fibbonacci series from {First} and {Second}:\n")
    for i in range(5):
        fib = First + Second
        Second = First
        First = fib
        1
        print(fib)

fib(a,b)
