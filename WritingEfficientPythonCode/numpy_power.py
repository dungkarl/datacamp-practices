import numpy as np

# python
nums = list(range(5))
print("python list:", nums)


nums_np = np.array(range(5))
print("numpy list:",nums_np)

num_np_ints = np.array([1,2,3,4])
print(num_np_ints.dtype)
print(nums_np.astype('float32'))
nums_np_floats = np.array([1, 2.5, 3])
print(nums_np_floats.dtype)

sqrt_num = []
for num in nums:
    sqrt_num.append(num**2)

print(sqrt_num)
sqrt_num_comp = [num**2 for num in nums if num%2==0]
print(sqrt_num_comp)
nums_np_new = np.array([-2, -1, 0, 1, 2])
print(nums_np_new**2)
print(nums[-1])
print(nums_np[-1])
