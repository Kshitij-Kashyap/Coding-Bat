def string_match(a, b):
  count = 0
  #assign the value of lowest length to n
  n = min(len(a),len(b))
  
  for i in range(n - 1):
    if a[i:i+2] == b[i:i+2]:
      count += 1

  return count
