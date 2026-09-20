def solution(rsp):
    # 이기는 경우를 매핑하는 딕셔너리 생성
    win_map = {
        "2": "0",  # 가위 -> 바위
        "0": "5",  # 바위 -> 보
        "5": "2",  # 보 -> 가위
    }

    # rsp의 각 문자를 이기는 값으로 변환하여 합치기
    return "".join(win_map[char] for char in rsp)