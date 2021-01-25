def binary_search(data, target, low, high):
    '''return true if target is found in indicated portion of a python list
    The search only considers the portion from data[low] to data[high] inclusive
    '''
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True 
        elif target < data[mid]:
            #recur on the portion left of the middle
            return binary_search(data, target, low, mid-1)
        else:
            #recur on the portion right of teh middle
            return binary_search(data, target, mid+1, high)
        
x = [1,2,3,4,5,6,7,8,9,10,11,12,13]

y = binary_search(x, 21,0,len(x) - 1)
print(y)