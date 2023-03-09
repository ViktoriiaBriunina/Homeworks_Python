def maximum(x,y,z):
    values = [x,y,z]
    maximum = values[0]
    for i in values:
        if i > maximum:
            maximum = i
    print(maximum)

maximum(100,200,300)


