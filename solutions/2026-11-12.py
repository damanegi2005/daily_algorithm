# 2026-11-12 | gcd

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
