def max_end3(nums):
  m = max(nums[0], nums[2])
  
  for i in range(len(nums)):
    nums[i] = m
    
  return nums
