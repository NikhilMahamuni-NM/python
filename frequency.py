
a1 = [13,12,11,13,14,13,7,11,13,14,12]
a2 = [13,12,11,13,14,13,7,11,13,14,12,14,14]
a3 = [13,12,11,13,14,13,7,11,13,14,12,14,14,7]

def frequency(arr):
    
    arr1 = set(arr)
    mi = len(arr)
    ma = 0

    minfreqlist = []
    maxfreqlist = []
    
    for i in arr1:
        count = arr.count(i)
        
        if count <= mi:
            mi = count
        elif count >= ma:
            ma = count

    for i in arr1:
        if arr.count(i) == mi:
            minfreqlist.append(i)
        elif arr.count(i) == ma:
            maxfreqlist.append(i)
       
    return(minfreqlist, maxfreqlist)

r1 = frequency(a1)
print(r1)
print(30*"-")
r2 = frequency(a2)
print(r2)
print(30*"-")
r3 = frequency(a3)
print(r3)
print(30*"-")
