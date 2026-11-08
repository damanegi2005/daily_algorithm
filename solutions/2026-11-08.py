# 2026-11-08 | count_vowels

def count_vowels(s):
    return sum(c.lower() in 'aeiou' for c in s)
