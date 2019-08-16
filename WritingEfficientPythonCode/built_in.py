

# generate
nums = range(5)
nums = list(nums)
print(nums)
"""
    ----------------
"""
# more efficient
nums_list2 = [*range(1,11,2)]
print(nums_list2)


# enumerate example
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
indexed_names = []
for i, name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names,0)]

print("Normal:", indexed_names)
print("Comprehension: ",indexed_names_comp)
print("Unpack:", indexed_names_unpack)
print(dict(indexed_names))

# map function example
names_map = map(str.upper, names)
print(type(names_map))
names_uppercase = [*names_map]
print(names_uppercase)
