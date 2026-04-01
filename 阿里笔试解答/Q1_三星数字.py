"""
阿里算法笔试 - 第一题（ACM 模式）

题意：
给定整数 n，寻找两个不同的正整数 x, y，满足：
1 <= x, y < n
x != y
n mod x == n mod y

如果有多组满足条件的答案，可以输出任意一组；
如果无解，输出 -1。

输入格式：
- 第一行：整数 T（1 <= T <= 10^4），表示测试数据组数。
- 接下来 T 行：每行一个整数 n（1 <= n <= 10^18）。

输出格式：
- 对于每组测试数据：
  - 若无解，输出一行 -1
  - 若有解，输出一行两个整数 x y（满足 1 <= x, y < n 且 x != y，且 n mod x == n mod y）

说明：
- 本题为“特判题”，有多解时输出任意一组合法解即可。
- 自测与判题展示可能出现“答案错误/特判提示”，需自行检查输出是否满足条件。

示例（题面展示）：
输入：
3
1
8
15

一种合法输出：
-1
2 4
3 5
"""

import sys

# ACM 顺序写法：不封装函数，按输入顺序直接处理
t_line = sys.stdin.readline().strip()
if t_line:
    t = int(t_line)
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        if n <= 3:
            print(-1)
        elif n % 2 == 0:
            print("1 2")
        else:
            print(f"2 {n - 1}")
