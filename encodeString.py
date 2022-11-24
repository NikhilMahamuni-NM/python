
MAX_CHAR = 26
 

def encodeString(string):
 
    hashEven = [0] * MAX_CHAR
    hashOdd = [0] * MAX_CHAR
 
    for i in range(len(string)):
        c = string[i]
        if i & 1: 
            hashOdd[ord(c) - ord('a')] += 1
        else:
            hashEven[ord(c) - ord('a')] += 1
 
    encoding = ""
    for i in range(MAX_CHAR):
        encoding += str(hashEven[i])
        encoding += str('-')
        encoding += str(hashOdd[i])
        encoding += str('-')
 
    return encoding
 

def countDistinct(input, n):
    countDist = 0 
 

    s = set()
    for i in range(n):

        if encodeString(input[i]) not in s:
            s.add(encodeString(input[i]))
            countDist += 1
 
    return countDist
 
# Driver Code
if __name__ == "__main__":
    input = ["abcd", "acbd", "adcb",
             "cdba", "bcda", "badc"]
    n = len(input)
    print(countDistinct(input, n))
