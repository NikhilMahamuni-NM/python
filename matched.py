
s1 = "zb%78"
s2 = "(7)(a"
s3 = "a)*(?"
s4 = "((jkl)78(A)&l(8(dd(FJI:),):)?)"

def matched(s):
    
    op = []

    for i in range(len(s)):
        if s[i] == '(':
            op.append(s[i])
        elif s[i] == ')':
            if len(op) != 0:
                op.pop()
                
    if len(op) == 0:
        return True
    else:
        return False

r1 = matched(s1)
print(r1)
print(30*"-")
r2 = matched(s2)
print(r2)
print(30*"-")
r3 = matched(s3)
print(r3)
print(30*"-")
r4 = matched(s4)
print(r4)


    
































