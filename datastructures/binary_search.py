def binary_search(list, target):
    first = 0
    last = len(list) -1
    
    while first <= last:
        
        """ 
        floor division operator 
        """
        
        midpoint = (first + last)//2 
        if list[midpoint] == target:
            return midpoint
        
        elif list[midpoint] < target:
            first = midpoint + 1
            
        else:
            last = midpoint -1
            
            return None
        
        
def verify(index):
    if binary_search is not None:
        print("target is found at: ", index)
        
    else:
        print("target not found")
        

    
list = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(list, 8)
verify(result)
        
            
            
     