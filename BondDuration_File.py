def getBondDuration(y, face, couponRate, m, ppy = 1):
  T = 0
  r = y / ppy
  N = m * ppy
  C = face * couponRate / ppy
  bondPrice = C * (1 - (1 + r) ** (-N)) / r + face / (1 + r) ** N
  T = 0.0
  for t in range(1, N + 1):
      cf = C
      if t == N:
          cf = cf + face
      T = T + (t / ppy) * (cf / (1 + r) ** t)  
    bondDuration = T / bondPrice
  return(bondDuration)
  


