def proc2(p):
    p = p + [1]    
    print p

p = [1, 2]
proc2(p)
print p

def proc2(p):
    p.append(1)
    print p

p = [1, 2]
proc2(p)
print p
