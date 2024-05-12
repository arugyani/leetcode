import types

def containsDuplicate(nums: list[int]) -> bool:
    vals = set()
    for n in nums:
        if n in vals: return True
        vals.add(n)
    return False

print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
