def solution(myString):
    return ''.join('l' if ch < 'l' else ch for ch in myString)