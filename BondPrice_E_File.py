<<<<<<< HEAD
def getBondPrice_E(face, couponRate, m, yc):
    C = face * couponRate    
    bondPrice = 0.0
    for t, y in enumerate(yc[:m], start=1):
        cf = C
        if t == m:
            cf += face       
        bondPrice += cf / (1 + y) ** t
    return bondPrice
=======
def getBondPrice_E(face, couponRate, m, yc):
    C = face * couponRate    
    bondPrice = 0.0
    for t, y in enumerate(yc[:m], start=1):
        cf = C
        if t == m:
            cf += face       
        bondPrice += cf / (1 + y) ** t
    return bondPrice
>>>>>>> 09ebeede1359a071488093f1fc59a4ebebb067a3
