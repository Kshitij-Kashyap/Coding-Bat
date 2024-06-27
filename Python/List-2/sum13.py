def sum13(nums):
    total_sum = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total_sum += nums[i]
            i += 1
    return total_sum

print(sum13([1, 2, 13, 2, 1, 13]))
