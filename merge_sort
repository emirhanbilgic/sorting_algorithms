L = [40, 2, 1, 21, 13, 23, 17, 11, 324, 112, 43, 5, 22]

def merge_sort(l):
    
    if len(l) > 1:
        
        # DIVIDING PART :
            
        left_side = l[:len(l)//2]
        right_side = l[len(l)//2:]
        merge_sort(left_side)
        merge_sort(right_side)
        print(left_side)
        print(right_side)
    
        # MERGING PART : 
        i=0
        j=0
        k=0 
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                l[k] = left_side[i]
                i += 1
            else:
                l[k] = right_side[j]
                j += 1
            k += 1    
        
        while i < len(left_side):
            l[k] = left_side[i]
            i += 1
            k += 1
        
        while j < len(right_side):
            l[k] = right_side[j]
            j += 1
            k += 1  
            
merge_sort(L)
print(L)
