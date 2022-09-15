L =[ 8, 3, 4, 5, 56, 1, 6, 2]

def insertion_sort(l):
    list_sorted = []
    list_unsorted = []
    list_sorted.append(l[0]) 
    l.pop(0)
    for each in l:
        list_unsorted.append(each)
    # print(list_unsorted)
    
    for i in range(len(l)):
        a = list_unsorted[0]
        list_sorted.append(a)
        list_unsorted.pop(0)
        for j in range(len(list_sorted)-1):
            if list_sorted[-1] < list_sorted[j]:
                list_sorted[j], list_sorted[-1] = list_sorted[-1], list_sorted[j]
                
        print(list_sorted)
        print(list_unsorted)
        
insertion_sort(L)  
    
