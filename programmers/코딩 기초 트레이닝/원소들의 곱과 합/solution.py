def solution(num_list):
    total = sum(num_list)
    
    mul = 1
    for n in num_list:
        mul *= n
        
    return 1 if total ** 2 > mul else 0