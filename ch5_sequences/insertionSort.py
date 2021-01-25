def insertion_sort(A):
    '''sort list of comparable elements into nondecreasing order.'''
    for k in range(1, len(A)): #from 1 to n-1
        current = A[k] #current element to be inserted
        j = k #correct index j for current
        while j > 0 and A[j-1] > current: #element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = current #current is now in the right place
    
    return A 

x = [5,4,6,3,7,2,1]
y = insertion_sort(x)
print(y)

