# To Generate all the sub sequence of list [3,2,1]
# [],[3],[2],[1],[3,2],[3,1],[3,2,1],[2,1]


numbers=[3,2,1]


def print_subsequence(idx,numbers,ls):
    
    if idx==len(numbers):
        print(ls)
        return
    
    # Take an element and add to list
    ls.append(numbers[idx])
    
    print_subsequence(idx+1,numbers,ls)
    
    # Once return back, we are not taking the added element and again generating the list
    
    ls.pop()
    print_subsequence(idx+1,numbers,ls)
    
    

# Function call

print_subsequence(0,numbers,[])
    