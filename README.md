# LeetCode

## 1. Two Sum

其他OJ的第一题一般都是A+B Problem，看题目名字
我也以为是那种水水的题目，最后发现并不是那么简单。
最开始直接在网页上面写了一个暴力方法求解的代码，
超时了。后面减小了循环内的运算量才过，不过还是暴力解法。
看到题解里面还可以用One-/Two- pass Hash的方法，觉得很不错。

## 2. Add Two Numbers

最开始题目没看懂，示例数据也没看明白。看了好长时间才发现
这好像就是小学生列竖式做加法一样。主要还是考察数据结构（链表）
的使用吧。

PS. LeetCode测试的时候只是调用那个规定好的函数，你写的其他的
代码不影响。

## 3. Longest Substring Without Repeating Characters

自己想了一个时间复杂度O(N logN)的算法，
利用Python内部的dict当做了Hash Table来做。
扫描一遍，遇到没出现过的字符就把它和它的位置加入dict，
更新最长的长度；遇到出现过，也更新最长的长度，同时更新dict中
该字符的位置和可以允许的子串起点位置。

## 4. Median of Two Sorted Arrays

将两个子串分别划分成为左右两段，然后调整划分位置，使得左右
数量平衡并且左边最大的不大于右边最小的。但是实际上提交，每次都能
遇到新的bug，比如奇数串左右划分的不均衡，出现空数据input``[]``
等。最后代码写下来不是很简洁。

## 10. Regular Expression Matching

想了一个递归的方法，实现起来不断的出了各种bug。当出现比较极端的
字符串的时候还出现了超时，于是又增加了数据的预处理来做剪枝，这才通过。
主要思想是对比扫描字符串，可能出现四种情况：
空、``.|[ch]``、``[ch]*``、``.*``，然后分别递归处理。
最后看来题解，正解是使用动态规划，还是Naive了，以前学的都忘记了。