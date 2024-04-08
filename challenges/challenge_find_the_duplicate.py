def find_duplicate(nums):
    if not (isinstance(nums, list) and len(nums) > 1):
        return False

    duplicate = set()

    for number in nums:
        if not (isinstance(number, int) and number >= 1):
            return False
        elif number in duplicate:
            return number
        else:
            duplicate.add(number)
    return False


# def find_duplicate(nums):
#     if not (isinstance(nums, list) and len(nums) > 1):
#         return False

#     try:
#         nums.sort()

#         for i in range(1, len(nums)):
#             if nums[i] >= 1 and nums[i] == nums[i - 1]:
#                 return nums[i]

#         return False

#     except Exception:
#         return False
