---
title: 2710. Remove Trailing Zeros From a String
tags:
  - String
  - Contest
---

## Problem Statement

---

Given a **positive** integer `num` represented as a string, return _the integer_ `num` _without trailing zeros as a string_.

**Example 1:**

```
Input: num = "51230100"
Output: "512301"
Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

```

**Example 2:**

```
Input: num = "123"
Output: "123"
Explanation: Integer "123" has no trailing zeros, we return integer "123".

```

**Constraints:**

- `1 <= num.length <= 1000`
- `num` consists of only digits.
- `num` doesn't have any leading zeros.

## Solution

```py
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        left, right = 0, len(num) - 1
        while(left < right):
            if(num[left] != '0' and num[right] != '0'):
                break;
            if(num[left] == '0'):
                left += 1
            if(num[right] == '0'):
                right -= 1
        return num[left: right + 1]
```
