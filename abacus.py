def abacus1(n):
    '''this print one line'''
    return '|'+"00000*****"[:10-n]+'   '+"00000*****"[10-n:]+'|'
def print_abacus(n):
    n = (10 - len( str(n) ) ) * '0' + str(n)
    for i in range(0,10):
        print abacus1(int(n[i]))

'''def print_abacus(value):
       #
       ### Add you code here 
       #

       part1|00000*****|
       part2 find space position
       part3 add space '   '

       string[:]+space''+string[:]

       0
1 line
1 line+ space
while
       '''



'''

string="00000*****"
space='   '
#print('|'+string+'|')
#print(0)
#print('|'+string+space+'|')
#print(1)
#print('|'+string[:-1]+space+string[-1:]+'|')

def abacus1(n):
    if n == 0:
        return '|00000*****   |'
    return '|'+string[:-n]+space+string[-n:]+'|'


def abacus2(n):
    n=str(n)
    length = len(n)
    
    #turn n to 000000n 0000000344
    n=(10-length)*'0'+n
    print n
    i=0
    result = ''
    for i in range(0,10):
        result = result+'\n'+abacus1(int(n[i]))

#    print string 
    #num=int(n[0])
    return result
print 'start'
#print abacus1(0)
#print abacus1(0)
print abacus2(344)
abacus2(45632)

'''


'''
###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|'''
print_abacus(12345678)
print_abacus(1098278)
