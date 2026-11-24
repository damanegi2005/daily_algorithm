# 2026-11-24 | gcd

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
