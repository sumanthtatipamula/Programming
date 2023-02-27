#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#
# https://leetcode.com/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (52.15%)
# Total Accepted:    113.8K
# Total Submissions: 217.6K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# A gene string can be represented by an 8-character long string, with choices
# from 'A', 'C', 'G', and 'T'.
# 
# Suppose we need to investigate a mutation from a gene string startGene to a
# gene string endGene where one mutation is defined as one single character
# changed in the gene string.
# 
# 
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# 
# 
# There is also a gene bank bank that records all the valid gene mutations. A
# gene must be in bank to make it a valid gene string.
# 
# Given the two gene strings startGene and endGene and the gene bank bank,
# return the minimum number of mutations needed to mutate from startGene to
# endGene. If there is no such a mutation, return -1.
# 
# Note that the starting point is assumed to be valid, so it might not be
# included in the bank.
# 
# 
# Example 1:
# 
# 
# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank =
# ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C',
# 'G', 'T'].
# 
# 
#
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        source, target, queue, processed, bankset = "", "", deque(), set(), set()
        def checkNeighbor(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        if(startGene == endGene):
            return 0
        queue.append(startGene)
        processed.add(startGene)
        level = 0
        while(queue):
            for _ in range(len(queue)):
                curr = queue.popleft()
                if(curr == endGene):
                    return level
                for mutation in bank:
                    if(checkNeighbor(mutation, curr) and mutation not in processed):
                        processed.add(mutation)
                        queue.append(mutation)
            level += 1
        return -1
        
