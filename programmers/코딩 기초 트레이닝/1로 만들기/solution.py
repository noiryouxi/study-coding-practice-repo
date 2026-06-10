def solution(num_list):
    return sum(n.bit_length() - 1 for n in num_list)