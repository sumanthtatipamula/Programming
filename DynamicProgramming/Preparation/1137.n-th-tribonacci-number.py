#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
# https://leetcode.com/problems/n-th-tribonacci-number/description/
#
# algorithms
# Easy (61.25%)
# Total Accepted:    375.4K
# Total Submissions: 593.4K
# Testcase Example:  '4'
#
# <p>The Tribonacci sequence T<sub>n</sub> is defined as follows:&nbsp;</p>
# 
# <p>T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, and
# T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub> for n
# &gt;= 0.</p>
# 
# <p>Given <code>n</code>, return the value of T<sub>n</sub>.</p>
# 
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# 
# <pre>
# <strong>Input:</strong> n = 4
# <strong>Output:</strong> 4
# <strong>Explanation:</strong>
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# </pre>
# 
# <p><strong class="example">Example 2:</strong></p>
# 
# <pre>
# <strong>Input:</strong> n = 25
# <strong>Output:</strong> 1389537
# </pre>
# 
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li><code>0 &lt;= n &lt;= 37</code></li>
# <li>The answer is guaranteed to fit within a 32-bit integer, ie. <code>answer
# &lt;= 2^31 - 1</code>.</li>
# </ul>
#
class Solution:
    def tribonacci(self, n: int) -> int:
        if(n <= 2):
            return 0 if(n == 0) else 1
        a, b, c = 0, 1, 1
        for i in range(2, n):
           a, b, c = b, c, a + b + c
        return c
        
