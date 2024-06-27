`def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

def round10(num):
  
  m = num % 10
  q = num // 10
  if m >= 5:
    q += 1
  return q * 10 
    
