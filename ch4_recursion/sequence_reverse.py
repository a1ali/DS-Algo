def reverse(S, start, stop):
    '''reverse elements in implicit slice S[start:stop]'''
    if start < stop - 1: #if at least 2 elements
        S[start], S[stop-1] = S[stop-1], S[start] #swap first and last
        reverse(S, start+1, stop-1) #recur on rest
    return S

x = [1,2,3,4,5,6,7]
y = reverse(x, 0, len(x))
print(y)