"""
[_arrow\_back_](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7)

Round A 2020 - Kick Start 2020

Practice mode

#### Practice Submissions

You have not attempted this problem.

Last updated: May 2 2023, 03:21

### Problem

Dr. Patel has **N** stacks of plates. Each stack contains **K** plates. Each plate has a positive _beauty value_, describing how beautiful it looks.

Dr. Patel would like to take exactly **P** plates to use for dinner tonight. If he would like to take a plate in a stack, he must also take all of the plates above it in that stack as well.

Help Dr. Patel pick the **P** plates that would maximize the total sum of beauty values.

### Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow. Each test case begins with a line containing the three integers **N**, **K** and **P**. Then, **N** lines follow. The i-th line contains **K** integers, describing the beauty values of each stack of plates from top to bottom.

### Output

For each test case, output one line containing `Case #x: y`, where `x` is the test case number (starting from 1) and `y` is the maximum total sum of beauty values that Dr. Patel could pick.

### Limits

Time limit: 20 seconds.  
Memory limit: 1 GB.  
1 ≤ **T** ≤ 100.  
1 ≤ **K** ≤ 30.  
1 ≤ **P** ≤ **N** \* **K**.  
The beauty values are between 1 and 100, inclusive.

#### Test Set 1

1 ≤ **N** ≤ 3.  

#### Test Set 2

1 ≤ **N** ≤ 50.  

### Sample

```
2
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10

```

```
Case #1: 250
Case #2: 180

```

In Sample Case #1, Dr. Patel needs to pick **P** = 5 plates:

-   He can pick the top 3 plates from the first stack (10 + 10 + 100 = 120).
-   He can pick the top 2 plates from the second stack (80 + 50 = 130) .

In total, the sum of beauty values is 250.

In Sample Case #2, Dr. Patel needs to pick **P** = 3 plates:

-   He can pick the top 2 plates from the first stack (80 + 80 = 160).
-   He can pick no plates from the second stack.
-   He can pick the top plate from the third stack (20).

In total, the sum of beauty values is 180.

**Note:** Unlike previous editions, in Kick Start 2020, all test sets are visible verdict test sets, meaning you receive instant feedback upon submission.
"""


def recursive_appraoch():
    for case in range(1, int(input()) + 1):
        (n, k, p) = map(int, input().split())
        plates = []
        for _ in range(n):
            plates.append(list(map(int, input().split())))
        for i in range(n):
            for j in range(1, k):
                plates[i][j] += plates[i][j - 1]
        mem = {}
        def maximizeBeauty(index, platesNeeded):
            if(platesNeeded == 0):
                return 0 
            if(index == n):
                return -float("Inf")
            if((index, platesNeeded) in mem):
                return mem[(index, platesNeeded)]
            beautyValue = maximizeBeauty(index + 1, platesNeeded)
            for i in range(k):
                if(i <= platesNeeded):
                    beautyValue = max(beautyValue, plates[index][i] + maximizeBeauty(index + 1, platesNeeded - i - 1))
            mem[(index, platesNeeded)] = beautyValue
            return mem[(index, platesNeeded)]
        print(f"Case #{case}: {maximizeBeauty(0, p)}")

def using_2d():
    for case in range(1, int(input()) + 1):
        (n, k, p) = map(int, input().split())
        plates = []
        for _ in range(n):
            plates.append(list(map(int, input().split())))
        for i in range(n):
            for j in range(1, k):
                plates[i][j] += plates[i][j - 1]
        dp = [[0] * (p + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, p + 1):
                dp[i][j] = dp[i - 1][j]
                for l in range(1, min(j + 1, k + 1)):
                    dp[i][j] = max(dp[i][j], plates[i - 1][l - 1] + dp[i - 1][j - l])           
        print(f"Case #{case}: {dp[n][p]}")

for case in range(1, int(input()) + 1):
    (n, k, p) = map(int, input().split())
    plates = []
    for _ in range(n):
        plates.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(1, k):
            plates[i][j] += plates[i][j - 1]
    dp = [0] * (p + 1)
    for i in range(1, n + 1):
        for j in range(p, 0, -1):
            for l in range(1, min(j + 1, k + 1)):
                dp[j] = max(dp[j], plates[i - 1][l - 1] + dp[j - l])           
    print(f"Case #{case}: {dp[p]}")



    

