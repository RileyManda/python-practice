def linear_search(list, result):
    """
    Returns the index position of the target else returns none
    """
    for i in range(0, len(list)):
        if list[i] == result:
            return i
    return None

def verify(index):
    if linear_search is not None:
        print("target is found at: ", index)
        
    else:
        print("target not found")
        

    
list = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(list, 10)
verify(result)

