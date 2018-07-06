def remove_adjacent(List):
    List=[1,2,2,4,4,5]
while i<len(List):
	if List[i] == List[i-1] :
		List.pop(i)
        i -= 1
    i += 1 
    return List