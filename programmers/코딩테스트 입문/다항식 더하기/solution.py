def solution(polynomial):
    x_sum = 0
    num_sum = 0

    for term in polynomial.split(" + "):
        if "x" in term:
            coef = term.replace("x", "")
            x_sum += int(coef) if coef else 1
        else:
            num_sum += int(term)

    result = ""

    if x_sum > 0:
        result += (str(x_sum) if x_sum > 1 else "") + "x"

    if num_sum > 0:
        if result:
            result += " + "
        result += str(num_sum)

    return result