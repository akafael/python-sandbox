def calc_binary_period(n):
    binary_digits = [0] * 30
    l = 0
    while (n > 0):
        binary_digits[l] = n % 2
        n //= 2
        l += 1
    for p in range(1, 1 + l):
        ok = True
        for i in range(l//2):
            if binary_digits[l-i] != binary_digits[l - i - p]:
                ok = False
                break
        if ok:
            return p
    return -1
