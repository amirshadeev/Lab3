def func(nums):
    list = []
    for i in nums:
        if i not in list:
            list.append(i)
    return list
nums = input("выведите лист:").split()
nums = list(map(int,nums))
func(nums)
print(func(nums))