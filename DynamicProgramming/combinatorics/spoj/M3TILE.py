"""
<table><tbody><tr><td><a href="https://www.spoj.com/problems/M3TILE/en/">English</a></td><td><a href="https://www.spoj.com/problems/M3TILE/vn/">Vietnamese</a></td></tr></tbody></table>

In how many ways can you tile a 3×n rectangle with 2×1 dominoes?

Here is a sample tiling of a 3×12 rectangle.

![](http://www.spoj.com/content/cyclops:m3tile.png)

Input consists of several test cases followed by a line containing -1. Each test case is a line containing an integer 0 ≤ n ≤ 30. For each test case, output one integer number giving the number of possible tilings.

### Example

```
Input:
2
8
12
-1

Output:
3
153
2131
```
"""
while(True):
    size = int(input())
    if(size == -1):
        break;
    f = [0] * (size + 2)
    g = [0] * (size + 2)
    f[0] = g[0] = 1
    f[1] = g[1] = 0
    for i in range(2, size + 1):
        f[i] = f[i - 2] + 2 * g[i - 2]
        g[i] = f[i] + g[i - 2]
    print(f[size])
