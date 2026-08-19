from math import gcd

def solution(a, b):
    # 기약분수로 약분
    b //= gcd(a, b)
    
    # 분모에서 2 제거
    while b % 2 == 0:
        b //= 2
    
    # 분모에서 5 제거
    while b % 5 == 0:
        b //= 5
    
    # 2와 5 외의 소인수가 없으면 유한소수
    return 1 if b == 1 else 2