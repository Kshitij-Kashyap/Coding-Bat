def cat_dog(str):
  countCat = countDog = 0
  
  for i in range(len(str)-2):
    if str[i:i+3] == 'cat':
      countCat += 1
    if str[i:i+3] == 'dog':
      countDog += 1

  return countCat == countDog

