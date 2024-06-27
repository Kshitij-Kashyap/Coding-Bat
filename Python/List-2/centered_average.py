def centered_average_v2(nums):
    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)
