import math
n = int(input("Enter Height: "))
m = int(input("Enter Width: "))

x = "-"
y = ".|."
z = "WELCOME"

q = ''

c = math.ceil(m/2)
w = c
a = 2
b = 1


for i in range(math.floor(n/2)):
    q = ((c-a)*x + b*y + (c-a)*x)
    print(q)
    c= c-3
    b = b+2

print((w-4)*x + z + (w-4)*x)

for i in range(math.floor(n/2)):
    c= c+3
    b = b-2
    q = ((c-a)*x + b*y + (c-a)*x)
    print(q)
