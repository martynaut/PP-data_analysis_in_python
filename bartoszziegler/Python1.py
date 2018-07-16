def prost(a, b):
    if a==b:
        print('to jest prostokąt')
    return 2*(a+b), a*b, 0.9*a*b
A = prost(3, 5)
print("obwod to", A[0])
print("pole to", A[1])
print("90% pola to ", A[2])