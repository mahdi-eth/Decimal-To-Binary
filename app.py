import math

def to_binary(n):
    n_tmp = n
    res = []
    while n_tmp > 0:
        rem = n_tmp % 2
        res.insert(0, rem)
        n_tmp = math.floor(n_tmp / 2)
    res_str = ''.join(str(e) for e in res)
    print(res_str)

n = abs(int(input("Enter a decimal number: ")))
to_binary(n)