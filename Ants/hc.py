import random

def randpass(len):
    str = []
    for i in range(len):
        c = random.randint(40,88)
        str.append(chr(c))
    return str

#a = input()

#s = list(a)
for length in range(1,12):
    for num in range(1,100):
        s = randpass(length)
        hash1 = 0
        hash2 = 0
        for i in range(len(s)):
            c = ord(s[i])
            hash1+= (c*c)**(i+1)
            c+=1
            hash2 += (c * c) ** (i + 1)
            s[i] = chr(c)
            #s1.append(s[i])
        print(s)
        print(hash1,"  ",hash2)