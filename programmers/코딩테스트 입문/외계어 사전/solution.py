def solution(spell, dic):
    target = ''.join(sorted(spell))
    
    for word in dic:
        if ''.join(sorted(word)) == target:
            return 1
    
    return 2