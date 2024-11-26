import math

def data_on_day(n):
    seen = set()
    k = 1
    while k <= n:
        value = math.floor(n/k)
        seen.add(value)
        next_k = n // value
        k = next_k + 1

    return sum(seen)
def test(n):
    seen = set()
    k = n + 1
    for i in range(k):
        if math.floor(n/k) not in seen:
            seen.add(math.floor(n/k))
        k-=1

    return sum(seen)


n = 10**10
# print(data_on_day(n))
print(test(n))