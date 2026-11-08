from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

EXAMPLES = [
    ('gcd', 'def gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n'),
    ('binary_search', 'def binary_search(a, x):\n    lo, hi = 0, len(a) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if a[mid] == x: return mid\n        if a[mid] < x: lo = mid + 1\n        else: hi = mid - 1\n    return -1\n'),
    ('palindrome', 'def is_palindrome(s):\n    return s == s[::-1]\n'),
    ('fibonacci', 'def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a\n'),
    ('prime', 'def is_prime(n):\n    if n < 2: return False\n    for i in range(2, int(n ** 0.5) + 1):\n        if n % i == 0: return False\n    return True\n'),
    ('two_sum', 'def two_sum(nums, target):\n    seen = {}\n    for i, x in enumerate(nums):\n        if target - x in seen: return [seen[target - x], i]\n        seen[x] = i\n    return []\n'),
    ('factorial', 'def factorial(n):\n    result = 1\n    for i in range(2, n + 1): result *= i\n    return result\n'),
    ('reverse_words', "def reverse_words(s):\n    return ' '.join(s.split()[::-1])\n"),
    ('count_vowels', "def count_vowels(s):\n    return sum(c.lower() in 'aeiou' for c in s)\n"),
    ('bubble_sort', 'def bubble_sort(a):\n    a = a[:]\n    for i in range(len(a)):\n        for j in range(len(a) - i - 1):\n            if a[j] > a[j + 1]: a[j], a[j + 1] = a[j + 1], a[j]\n    return a\n'),
    ('prefix_sum', 'def prefix_sum(a):\n    result = [0]\n    for x in a: result.append(result[-1] + x)\n    return result\n'),
    ('valid_parentheses', "def valid_parentheses(s):\n    depth = 0\n    for c in s:\n        depth += (c == '(') - (c == ')')\n        if depth < 0: return False\n    return depth == 0\n"),
]

today = datetime.now(ZoneInfo('Asia/Seoul')).date()
name, code = EXAMPLES[today.toordinal() % len(EXAMPLES)]
path = Path('solutions') / f'{today.isoformat()}.py'
path.parent.mkdir(parents=True, exist_ok=True)
if not path.exists():
    path.write_text(f'# {today.isoformat()} | {name}\n\n{code}', encoding='utf-8')
    print(f'Created {path}')
else:
    print(f'Already exists: {path}')
