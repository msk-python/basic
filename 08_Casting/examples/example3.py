A = 12      # int
B = 2.8     # float
C = "3"     # string
D = "4.2"   # float in string

a = int(A)
b = int(B)
c = int(C)
# d = int(D) # D will be error use first float then convert to int

x = float(D)  # return: 4.2 (float value)
y = int(x)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(y, type(y))