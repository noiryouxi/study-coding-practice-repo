def solution(num_list):
    even = ''.join(str(i) for i in num_list if i % 2 == 0)
    odd = ''.join(str(i) for i in num_list if i % 2 == 1)
    
    return int(even) + int(odd)