def factorial(n):
    if n!=1:
        return factorial(n-1)*n
    else:
        return 1

print(str(factorial(int(input("Number to factorise: ")))))