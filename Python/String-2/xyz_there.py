def xyz_there(str):
  for i in range(len(str) - 2):
    if str[i - 1] != '.' and str[i:i+3] == 'xyz':
      return True
  return False

