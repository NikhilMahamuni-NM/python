import math

string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
width = 4

iterations = math.ceil(len(string)/4)
i=0
ini = 0
j=0

while j < iterations:
    
    wid = ini+4
    print(ini,width)
    #print(string[ini:wid])
    i += width
    ini=i 
    j += 1
        
def wrap(string, width):
    iterations = math.ceil(len(string)/4)
    i=0
    ini = 0
    j=0
    arr = []
    while j < iterations:
        
        wid = ini+width
        arr.append(ini)
        #print(string[ini:wid])
        i += width
        ini=i 
        j += 1
    k=0
    s = ''
    while k < iterations:
        #print(string[arr[k]:arr[k]+width])
        if k == iterations-1:
            s = s + string[arr[k]:arr[k]+width]
        else:
            s = s + string[arr[k]:arr[k]+width] + '\n'
        k += 1
    return s
print(wrap(string,width))
