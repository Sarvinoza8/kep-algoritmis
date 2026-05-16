import math

n = int(input())
sami = 0

for i in range(1, n + 1):
    sami += int(math.isqrt(i)) # math.isqrt(i) ildizning butun qismini qaytaradi

print(sami)
