
a = 9
ar = [10,20,20,10,10,30,50,10,20]
nos = []
for i in range(1,101):
    nos.append(i)
tot = []
for j in nos:
    c = ar.count(j)
    if c / 2 >= 1:
        tot.append(int(c/2))

print(sum(tot))

