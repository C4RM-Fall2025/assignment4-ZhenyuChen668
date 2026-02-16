<<<<<<< HEAD
def getBondPrice_Z(face, couponRate, times, yc):
    C = face * couponRate
    bondPrice = 0.0
    for t, y in zip(times, yc):
        cf = C
        if t == times[-1]:
            cf = cf + face
        bondPrice += cf / (1 + y) ** t
    return bondPrice
=======
def getBondPrice_Z(face, couponRate, times, yc):
    C = face * couponRate
    bondPrice = 0.0
    for t, y in zip(times, yc):
        cf = C
        if t == times[-1]:
            cf = cf + face
        bondPrice += cf / (1 + y) ** t
    return bondPrice
>>>>>>> 09ebeede1359a071488093f1fc59a4ebebb067a3
