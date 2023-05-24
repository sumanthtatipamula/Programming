---
title: K-periodic Circular String
tags:
  - Strings
  - Contest
  - HashMap
---

A **K**\-periodic circular string is a circular string which remains same when it is rotated by K units.  
Given a circular string **s**, find whether there exists a permuation of s which is a K-periodic circular string and if it exists then find lexicographically smallest permuation of s which is a K-periodic circular string. Return empty string if there does not exist a valid permutation of s which is a K-periodic circular string.  
**Note**: You can rotate string in any direction.

**Example 1:**

```
Input:
s = "abba"
K = 2
Output:
abab
Explanation:
"abab" when rotated by 2 units remains
same.

```

**Example 2:**

```
Input:
s = "abbbbbb"
K = 4
Output:
-1
Explanation:
No permuation of s can be a 4-periodic
circular string.

```

**Your Task:**  
You don't need to read input or print anything. Your task is to complete the function **kPeriodic()** which takes the string **s** and integer **K** as input parameters and returns the lexicographically smallest permuation of s which is a K-periodic circular string if it exists, else returns an empty string, the driver code will print "-1" in that case.

**Expected Time Complexity:** O(|s|)  
**Expected Auxiliary Space:** O(|s|)

**Constraints:**  
1 ≤ |s| ≤ 10<sup>5</sup>  
1 ≤ K ≤ 10<sup>9</sup>

```python

class Solution:
    def kPeriodic(self, s, k):
        freq = [0] * 26
        different_chars = 0
        current_char = ''
        for char in s:
            freq[ord(char) - ord('a')] += 1
            if(freq[ord(char) - ord('a')] == 1):
                different_chars += 1
                current_char = 'a'
        size, index = 0, 0
        result = ['-'] * len(s)
        while(result[index] == '-'):
            size += 1
            result[index] = '.'
            index += k
            index %= len(s)
        for i in range(26):
            if(freq[i] % size != 0):
                return ""
        result = ['-'] * len(s)
        cnt, index, charindex = 0, 0, 0
        while(cnt < len(s)):
            while(result[index] != '-'): index += 1
            while(freq[charindex] == 0): charindex += 1
            while(result[index] == '-'):
                cnt += 1
                result[index] = chr(ord('a') + charindex)
                index += k
                index %= len(s)
            freq[charindex] -= size
        return ''.join(result)

```
