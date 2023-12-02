def bank(x,y):
    if y > 0:
        for i in range(1,y+1):
            x = x*1.1
        return x
    else: return x
