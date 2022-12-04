class Solution {

    public int minimumAverageDifference(int[] nums) {
        int n = nums.length, minDiff = Integer.MAX_VALUE, minDiffIndex = 0;
        long leftSum = 0, rightSum = 0, sum = 0;
        for (int i = 0; i < n; i++) sum += nums[i];

        for (int i = 0; i < n; i++) {
            leftSum += nums[i];
            rightSum = sum - leftSum;

            int leftAvg = (int) (leftSum / (i + 1));
            int rightAvg = (int) (i == n - 1 ? 0 : rightSum / (n - i - 1));

            int currDiff = Math.abs(leftAvg - rightAvg);

            if (currDiff < minDiff) {
                minDiff = currDiff;
                minDiffIndex = i;
            }
        }

        return minDiffIndex;
    }
}
