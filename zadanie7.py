#1
"""for x in range(15):
    total = 110303 + 3390 * x 
    if total % 14 == 0:
        print(f"1: x={x}, частное={total//14}")
        break"""
#2
"""sum_digits = 98
for p in range(16, 100):
    if sum_digits % (p-1) == 0:
        print(f"2: p={p}")
        break"""
#3
"""for x in range(10):
    total = 8288 * x + 5206
    if total % 155 == 0:
        print(f"3: x={x}, частное={total//155}")
        break"""
#4
"""best = None
for y in range(8):
    for x in range(8):
        total = 14642 * y + 19 * x + 11433  
        if total % 117 == 0:
            if best is None or total < best[0]:
                best = (total, x, y, total//117)

print(f"4: x={best[1]}, y={best[2]}, частное={best[3]}")"""
#5 
"""import sys

value = 7 * pow(8, 5736) + 6 * pow(8, 3908) - 5 * pow(81, 991) - 4 * pow(81, 980) - 2022


oct_str = oct(value)[2:]  
count_7 = oct_str.count('7')

print(f"Ответ 5: количество цифр 7 = {count_7}")"""