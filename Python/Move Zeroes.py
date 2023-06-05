def move_zeros_to_end(nums):
  non_zero_index = 0

  for i in range(len(nums)):
    if nums[i] != 0:
      nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
      non_zero_index += 1

  for i in range(non_zero_index, len(nums)):
    nums[i] = 0

  return nums


if __name__ == "__main__":
  nums = [0, 1, 0, 3, 12, 0]
  nums = move_zeros_to_end(nums)
  print(nums)
