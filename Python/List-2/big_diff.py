def big_diff(nums):
  minimum = maximum = nums[0]
  for num in nums[1:]:
      if num < minimum:
          minimum = num
      elif num > maximum:
          maximum = num
  return maximum - minimum
