test_bank = [0,2,7,0]

l = [0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]
cycles = 0
prevs = []

while l not in prevs:
    prevs.append(l[:])
    m = max(l)
    i = l.index(m)
    l[i] = 0
    while m:
        i=(i+1)%len(l)
        l[i]+=1
        m-=1
    cycles+=1

print(cycles)
print(len(prevs)-prevs.index(l))#part 2
