# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


def symmetric(mylist):
    
    # compare the j row and collumn
    for j in range(len(mylist)):
        row = mylist[j]

        # generate column
        column= []
        for i in range(len(mylist)):
            column += [mylist[i][j]]
            
        if row != column:
            return False
    return True

def symmetric_draft1(mylist):
    # Your code here
    
    
    for j in range(len(mylist)):
        # row(0) 
        row = mylist[j]
        column= []
        for i in range(len(mylist)):
            #print i
            # column(0) = mylist[0][0] + mylist[1][0] + [2][0]
            column += [mylist[i][j]]
        #print 'row'
        #print row
        #print 'column'
        #print column
        if row != column:
            return False
    return True
    

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False
