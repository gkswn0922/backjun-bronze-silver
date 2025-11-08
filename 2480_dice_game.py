a, b, c = map(int, input().split())

if a == b == c:
    result = 10000 + a * 1000


if a == b and b != c:
    result = 1000 + a * 100


if b == c and b != a:
    result = 1000 + b * 100


if a == c and b != a:
    result = 1000 + a * 100


if a != b and b != c and c != a:
    if a > b and a > c:
        result = a * 100
    if b > c and b > a:
        result = b * 100
    if c > a and c > b:
        result = c * 100


print(result)
