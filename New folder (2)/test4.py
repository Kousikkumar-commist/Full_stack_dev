x=10
print(id(x))
a = 10
b = 10
print(id(a))  # This might be the same as id(b) due to optimization.
print(id(b))

c = 1000
d = 1000
print(id(c))  # This might be different from id(d) because the value is larger.
print(id(d))
