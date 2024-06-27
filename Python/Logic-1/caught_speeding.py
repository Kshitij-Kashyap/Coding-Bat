def caught_speeding(speed, is_birthday):
  s = 0
  if is_birthday:
    s += 5
  if speed <= 60 + s:
    return 0
  if 61 <= speed and speed <= 80 + s:
    return 1
  return 2

