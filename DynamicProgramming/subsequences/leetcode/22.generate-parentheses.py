#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (68.59%)
# Total Accepted:    988.3K
# Total Submissions: 1.4M
# Testcase Example:  '3'
#
# <p>Given <code>n</code> pairs of parentheses, write a function to
# <em>generate all combinations of well-formed parentheses</em>.</p>
# 
# <p>&nbsp;</p>
# <p><strong>Example 1:</strong></p>
# <pre><strong>Input:</strong> n = 3
# <strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
# </pre><p><strong>Example 2:</strong></p>
# <pre><strong>Input:</strong> n = 1
# <strong>Output:</strong> ["()"]
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# 
# <ul>
# <li><code>1 &lt;= n &lt;= 8</code></li>
# </ul>
# 
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(open, closed, string):
            if(open == closed and closed == n):
                result.append(string)
                return
            elif(open == n or open > closed):
                generate(open, closed + 1, string + ')')
            if(open < n):
                generate(open + 1, closed, string + '(')
        generate(0, 0, "")
        return result

