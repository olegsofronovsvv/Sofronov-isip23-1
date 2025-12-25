#1
"""def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)



print(factorial(1))   
print(factorial(2))   
print(factorial(3))   
print(factorial(4))   
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))"""
#2
"""def remove_vowels(string):
    glasnie = ['a', 'o', 'e', 'i', 'u', 'y']
    vivod = ''
    for bukva in string:
        if bukva not in glasnie:
            vivod += bukva
    return vivod
n = input()
print(remove_vowels(n))"""
#3
N = 3
P = [ ]
for i in range(N):
    row = [1] * (i+1)
    row j in range(i+1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]
