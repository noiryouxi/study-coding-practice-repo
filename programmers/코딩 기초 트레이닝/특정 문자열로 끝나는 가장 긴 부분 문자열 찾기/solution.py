def solution(myString, pat):
    idx = myString.rfind(pat)  # pat의 마지막 위치
    return myString[:idx + len(pat)]