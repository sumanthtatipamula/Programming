class Solution:
    def rangeOR(self, n):
        ans = 1
        while(ans <= n):
            ans *= 2
        ans -= 1
        return ans