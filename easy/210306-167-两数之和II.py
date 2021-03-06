"""
给定一个已按照 升序排列 的整数数组numbers ，请你从数组中找出两个数满足相加之和等于目标数target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。


示例 1：

输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
示例 2：

输入：numbers = [2,3,4], target = 6
输出：[1,3]
示例 3：

输入：numbers = [-1,0], target = -1
输出：[1,2]


提示：

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers 按 递增顺序 排列
-1000 <= target <= 1000
仅存在一个有效答案

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        双指针法
        a 指针从左向右， b指针从右向左
        由于数组是有序的，a 指针向右滑动时，数字是在不断增大，所以 b指针只能向左滑动
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        b = len(numbers) - 1
        while(a < b):
            if numbers[a] + numbers[b] == target:
                break
            if numbers[a] + numbers[b] > target:
                b -= 1
            else:
                a += 1
        return [a+1, b+1]

if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15],9))