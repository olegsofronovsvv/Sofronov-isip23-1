#1
"""def paths(a, b):
    ways = [0] * (b + 1)
    ways[a] = 1
    
    for i in range(a, b + 1):
        if ways[i] > 0:
            if i + 1 <= b:
                ways[i + 1] += ways[i]
            if i + 2 <= b:
                ways[i + 2] += ways[i]
            if i * 2 <= b:
                ways[i * 2] += ways[i]
    
    return ways[b]


result = paths(3, 10) * paths(10, 12)
print(result)"""
#2
"""def paths(start, end, bad):
    ways = [0] * (end + 1)
    ways[start] = 1
    
    for i in range(start, end + 1):
        if i == bad or ways[i] == 0:
            continue
        
        
        if i + 1 <= end:
            ways[i + 1] += ways[i]
        
        
        if 2 * i + 1 <= end:
            ways[2 * i + 1] += ways[i]
    
    return ways[end]

result = paths(1, 27, 26)
print(result)"""
#3
"""def paths(start, end, bad):
    ways = [0] * (end + 1)
    ways[start] = 1
    
    for i in range(start, end + 1):
        if i == bad or ways[i] == 0:
            continue
        
    
        if i + 1 <= end:
            ways[i + 1] += ways[i]
        
        
        if i + 2 <= end:
            ways[i + 2] += ways[i]
    
    return ways[end]


result = paths(2, 9, 14) * paths(9, 18, 14)
print(result)"""
