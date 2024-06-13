# 冒泡排序

nums = [3, 9, 5, 2, 6, 7]

for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        # print(nums)
print(nums)
