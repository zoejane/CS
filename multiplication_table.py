def print_multiplication_table(n):
    i=1
    while i<n+1:
        #print "entry i loop "+str(i)
        #print(str(i)+'*'+str(j)+'='+str(i*j))

        j=1
        while j<=n:
            #print 'entry j loop '+str(j)
            print(str(i)+'*'+str(j)+'='+str(i*j))
            j = j+1
            
        i=i+1
        
       
    


#print_multiplication_table(2)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4

print_multiplication_table(3)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 1 * 3 = 3
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4
#>>> 2 * 3 = 6
#>>> 3 * 1 = 3
#>>> 3 * 2 = 6
#>>> 3 * 3 = 9


