def solution(expressions):
    answer = []

    # 가능한 진법 탐색
    candidates = []

    for base in range(2, 10):
        valid = True

        for exp in expressions:
            a, op, b, _, c = exp.split()

            # X가 아닌 숫자가 해당 진법에서 유효한지 확인
            if any(int(ch) >= base for ch in a + b + (c if c != 'X' else '')):
                valid = False
                break

            # 결과가 주어진 수식이라면 검증
            if c != 'X':
                a_num = int(a, base)
                b_num = int(b, base)
                c_num = int(c, base)

                if op == '+':
                    result = a_num + b_num
                else:
                    result = a_num - b_num

                if result != c_num:
                    valid = False
                    break

        if valid:
            candidates.append(base)

    # X가 있는 수식의 결과 계산
    for exp in expressions:
        a, op, b, _, c = exp.split()

        if c != 'X':
            continue

        results = set()

        for base in candidates:
            a_num = int(a, base)
            b_num = int(b, base)

            if op == '+':
                result = a_num + b_num
            else:
                result = a_num - b_num

            # 해당 진법의 문자열로 변환
            def convert(n, base):
                if n == 0:
                    return '0'

                digits = ''
                while n > 0:
                    digits = str(n % base) + digits
                    n //= base

                return digits

            results.add(convert(result, base))

        # 모든 진법에서 결과가 같으면 해당 결과, 아니면 ?
        if len(results) == 1:
            answer.append(exp.replace('X', results.pop()))
        else:
            answer.append(exp.replace('X', '?'))

    return answer