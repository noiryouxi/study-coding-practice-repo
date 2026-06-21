import re

def solution(myStr):
    result = [s for s in re.split('[abc]', myStr) if s]
    return result if result else ["EMPTY"]