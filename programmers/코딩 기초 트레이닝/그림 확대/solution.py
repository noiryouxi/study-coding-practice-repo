def solution(picture, k):
    answer = []
    for row in picture:
        enlarged = ''.join(ch * k for ch in row)
        answer.extend([enlarged] * k)
    return answer