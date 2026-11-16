def solution(data, ext, val_ext, sort_by):
    columns = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    ext_idx = columns[ext]
    sort_idx = columns[sort_by]

    answer = [row for row in data if row[ext_idx] < val_ext]
    answer.sort(key=lambda x: x[sort_idx])

    return answer