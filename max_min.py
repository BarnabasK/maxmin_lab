def find_max_min(numbers):
  
    min_num=min(numbers)
    max_num=max(numbers)
    
    if max_num != min_num:
      return [min_num,max_num]
    else:
	return [len(numbers)]

print find_max_min([1,4,7,2,8])
print find_max_min([41,42])