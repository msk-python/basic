A = 12      # int
B = 2.8     # float
C = "3"     # string
D = "4.2"   # float in string

print(type(A))
print(type(B))
print(type(C))
print(type(D))

A = int(A)
B = int(B)
C = int(C)
D = int(D) # D will be error use first float then convert to int

print("Type of A : " , type(A))
print("Type of B : " , type(B))
print("Type of C : " , type(C))
# print("Type of D : " , type(D))  