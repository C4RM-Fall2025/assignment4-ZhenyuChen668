<<<<<<< HEAD
def getBondPrice(y, face, couponRate, m, ppy=1):
    r = y / ppy
    N = m * ppy
    C = face * couponRate / ppy
    bondPrice = C * (1 - (1 + r) ** (-N)) / r + face / (1 + r) ** N
    return(bondPrice)
=======
def getBondPrice(y, face, couponRate, m, ppy=1):
    r = y / ppy
    N = m * ppy
    C = face * couponRate / ppy
    bondPrice = C * (1 - (1 + r) ** (-N)) / r + face / (1 + r) ** N
    return(bondPrice)

>>>>>>> 09ebeede1359a071488093f1fc59a4ebebb067a3
