# 217. Contains Duplicate
![Easy](https://img.shields.io/badge/-Easy-90EE90?style=flat&color=90EE90)

# Description
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1:**
> **Input:** `nums = [1, 2, 3, 1]`
>
> **Output:** `true`

**Example 2:**
> **Input:** `nums = [1, 2, 3, 4]`
> 
> **Output:** `false`

**Example 3:**
> **Input:** `nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]`
>
> **Output:** `true`

<br>

**Constraints:**
- $1 \leq \text{nums.length} \leq 10^5$
- $-10^9 \leq \text{nums[i]} \leq 10^9$

# Solution

**Python**
```python
def containsDuplicate(nums):
    vals = set()
    for n in nums:
        if n in vals: return True
        vals.add(n)
    return False
```

We choose `set()` as the data structure to hold our values because it does not allow duplicates. Meaning during our search through `nums`, if we encounter a value *n* that already exists inside the set `vals`, then it is a duplicate. <u>This means that we have found a duplicate</u>.
