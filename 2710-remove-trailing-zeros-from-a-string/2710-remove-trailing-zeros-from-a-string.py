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
        