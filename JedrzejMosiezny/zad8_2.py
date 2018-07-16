def field(a, b):
    if a==b:
        print("Jest kwadratem")
    return (2*(a+b)), (a*b), (0.9*(a*b))

A = field(4, 4)
print(A)