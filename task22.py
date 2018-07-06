def last(n):
    return n[0]  
 
def sort(tuples):
    return sorted(tuples, key=last)
print(sort([(1,2),(2,3),(4,1),(7,4)]))

