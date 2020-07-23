def persistence(n):
    # your code
    if n < 10:
        return 0
    else:
        product = 1
        while n != 0:
            product *= (n % 10)
            n //= 10
        return 1 + persistence(product)