def sum_ignore_67(nums):
    total_sum = 0
    skip_section = False

    for num in nums:
        if num == 6:
            skip_section = True
        elif num == 7 and skip_section:
            skip_section = False
        elif not skip_section:
            total_sum += num

    return total_sum

