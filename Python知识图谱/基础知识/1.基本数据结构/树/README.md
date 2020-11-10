## LeetCode 学习树的知识点
https://leetcode-cn.com/leetbook/detail/data-structure-binary-tree/

## Pre-Order Traversal
先序遍历（前序遍历）

## In-Order Traversal
中序遍历(二叉树)

## Post-Order Traversal
后序遍历

## Recursive
递归（利用系统堆栈展开运算）

## Iterative
迭代（循环，一次展开部分进行运算）

## 总结
总体来说，无论是利用递归还是迭代，他们都是重复针对当前节点的（左、自身、右）来进行操作；
递归可以很直观的给出代码模板，而迭代需要在栈顶元素进行分支展开，依据前序、中序、后序操作顺序的不同，
给出迥异的入栈、出栈方式。

这里给出一份特别的迭代法解法，我理解为二分选择法：
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/er-cha-shu-de-suo-you-bian-li-fang-fa-jian-ji-ming/

初始条件和我默认的方式一样，`stack` 栈 和 `current` 指针，但是它的循环体是对当前节点进行左右分支方向选择，
而不是对当前节点进行操作，导致了理解上的差异。