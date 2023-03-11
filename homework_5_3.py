def fact(x):
    """Calculate a Factorial for number X"""
    answer = 1
    for i in range(1, x + 1):
        answer = answer * i
    return answer

print(fact(5))

for i in range (5):
    print(fact(i))
