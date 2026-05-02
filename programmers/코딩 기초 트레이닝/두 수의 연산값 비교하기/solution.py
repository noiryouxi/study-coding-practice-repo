def solution(a, b):

    concat = int(str(a) + str(b))
    mul = 2 * a * b
    
    return concat if concat >= mul else mul
 