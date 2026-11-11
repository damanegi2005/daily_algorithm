# 2026-11-11 | valid_parentheses

def valid_parentheses(s):
    depth = 0
    for c in s:
        depth += (c == '(') - (c == ')')
        if depth < 0: return False
    return depth == 0
