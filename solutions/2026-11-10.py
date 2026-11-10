# 2026-11-10 | prefix_sum

def prefix_sum(a):
    result = [0]
    for x in a: result.append(result[-1] + x)
    return result
