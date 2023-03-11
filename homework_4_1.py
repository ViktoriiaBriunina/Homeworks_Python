def maximum(x,y,z):
    """Find a maximum"""
    values = [x, y ,z]
    maximum = values[0]
    for i in values:
        if i > maximum:
            maximum = i
    return maximum
print(maximum(400,200,300))


