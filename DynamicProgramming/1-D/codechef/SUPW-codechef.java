/**
 * ## Problem
 * https://www.codechef.com/ZCOPRAC/problems/ZCO14002

## Zonal Computing Olympiad 2014, 30 Nov 2013

In ICO School, all students have to participate regularly in SUPW. There is a different SUPW activity each day, and each activity has its own duration. The SUPW schedule for the next term has been announced, including information about the number of minutes taken by each activity.

Nikhil has been designated SUPW coordinator. His task is to assign SUPW duties to students, including himself. The school's rules say that no student can go three days in a row without any SUPW duty.

Nikhil wants to find an assignment of SUPW duty for himself that minimizes the number of minutes he spends overall on SUPW.

  

### Input format

Line 1: A single integer _N_, the number of days in the future for which SUPW data is available.

Line 2: _N_ non-negative integers, where the integer in position _i_ represents the number of minutes required for SUPW work on day _i_.

  

### Output format

The output consists of a single non-negative integer, the minimum number of minutes that Nikhil needs to spend on SUPW duties this term

  

### Sample Input 1

```
10
3 2 1 1 2 3 1 3 2 1

```

  

### Sample Output 1

```
4

```

(Explanation: 1+1+1+1)

  

### Sample Input 2

```
8
3 2 3 2 3 5 1 3

```

  

### Sample Output 2

```
5

```

(Explanation: 2+2+1)

  

### Test data

There is only one subtask worth 100 marks. In all inputs:

• 1 ≤ _N_ ≤ 2×10<sup>5</sup>

• The number of minutes of SUPW each day is between 0 and 10<sup>4</sup>, inclusive.

  

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
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = scan.nextInt();
    }
    if (n < 3) {
      if (n == 1) System.out.println(arr[0]); else System.out.println(
        Math.min(arr[0], arr[1])
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
    System.out.println(Math.min(dp[n - 1], Math.min(dp[n - 2], dp[n - 3])));
  }
}
