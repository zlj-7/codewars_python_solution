def solution(number):
    # TODO: implement
    number -= 1
    sum_ = sum_part(number // 3, 3) + sum_part(number // 5, 5)
    if number >= 15:
        sum_ -= 3 * sum_part(number // 15, 5)
    return sum_

def sum_part(num, base):
    return (base*(num+1)*num) // 2