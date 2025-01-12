def single_number(nums):
    for i in nums:
        if nums.count(i) == 1:
            return i

numbers = [2, 3, 2, 4, 3]

print(f"single number:", single_number(numbers))
