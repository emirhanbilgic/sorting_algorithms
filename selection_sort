L = [40, 2, 21, 13, 23, 17, 11, 324, 112, 43, 5, 22, 1]


def def_min(l):
    i = 0
    while i < len(l):
        if l[i] < l[0]:
           l[0] , l[i] = l[i] , l[0]
        i +=1 
  
    return l
  
    
def selection_sort(l):
    sorted_list = []
    while len(l) >= 1:
        def_min(l) 
        sorted_list.append(l[0])
        l.pop(0)
        
    return sorted_list
