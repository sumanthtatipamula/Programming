/**
 * ## Problem
 * https://www.codechef.com/ZCOPRAC/problems/ZCO14004

## Zonal Computing Olympiad 2014, 30 Nov 2013

In IPL 2025, the amount that each player is paid varies from match to match. The match fee depends on the quality of opposition, the venue etc.

The match fees for each match in the new season have been announced in advance. Each team has to enforce a mandatory rotation policy so that no player ever plays three matches in a row during the season.

Nikhil is the captain and chooses the team for each match. He wants to allocate a playing schedule for himself to maximize his earnings through match fees during the season.

  

### Input format

Line 1: A single integer _N_, the number of games in the IPL season.

Line 2: _N_ non-negative integers, where the integer in position _i_ represents the fee for match _i_.

  

### Output format

The output consists of a single non-negative integer, the maximum amount of money that Nikhil can earn during this IPL season.

  

### Sample Input 1

```
5 
10 3 5 7 3 

```

  

### Sample Output 1

```
23

```

(Explanation: 10+3+7+3)

  

### Sample Input 2

```
8
3 2 3 2 3 5 1 3

```

  

### Sample Output 2

```
17

```

(Explanation: 3+3+3+5+3)

  

### Test data

There is only one subtask worth 100 marks. In all inputs:

• 1 ≤ _N_ ≤ 2×10<sup>5</sup>

• The fee for each match is between 0 and 10<sup>4</sup>, inclusive.

  

### Live evaluation data

There are 12 test inputs on the server during the exam.
 */

/* package codechef; // don't place package name! */

import java.io.*;
import java.lang.*;
import java.util.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef {

  public static void main(String[] args) throws java.lang.Exception {
    Scanner scan = new Scanner(System.in);
    int n = scan.nextInt();
    int total = 0;
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = scan.nextInt();
      total += arr[i];
    }
    if (n < 3) {
      if (n == 1) System.out.println(arr[0]); else System.out.println(
        arr[0] + arr[1]
      );
      return;
    }
    int dp[] = new int[n];
    // dp[i] -> minimum number of minutes in SUPW duty if a[0...i] and the duty ends on ith day.
    for (int i = 0; i < n; i++) {
      dp[i] = arr[i];
      if (i - 3 >= 0) {
        dp[i] += Math.min(dp[i - 1], Math.min(dp[i - 2], dp[i - 3]));
      }
    }
    System.out.println(
      total - (Math.min(dp[n - 1], Math.min(dp[n - 2], dp[n - 3])))
    );
  }
}
