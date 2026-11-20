# 2026-11-20 | count_vowels

def count_vowels(s):
    return sum(c.lower() in 'aeiou' for c in s)
