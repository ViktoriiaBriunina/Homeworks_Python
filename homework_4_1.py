def maximum(x,y,z):
    values = [x,y,z]
    maximum = values[0]
    for i in values:
        if i > maximum:
            maximum = i
    return maximum
print(maximum(100,200,300))


