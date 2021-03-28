"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组[0,1,2,4,5,6,7] 可能变为[4,5,6,7,0,1,2])。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是寻找旋转排序数组中的最小值的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def findMin(self, nums):
        """
                                 [ /  ]
        数组中的数字以折线图表示 为一个[   /]的图像， 两个递增的斜线，第二个斜线低位为最小值。
        则进行二分查找 k = len(num)/2
        如果 num[k] < 右边界，则说明在第二条斜线上，排除右边数组
        如果 num[k] > 右边界，说明在 第一条斜线上，排除左边界
        相同时，无法判断，则右边界左移
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while (l < r):
            k = int(l + (r-l)/2)
            # print(l, r, k, nums[k], nums[r])
            if nums[k] > nums[r]:
                l = k + 1
            elif nums[k] < nums[r]:
                r = k
            else:
                r -= 1

        return nums[l]



if __name__ == "__main__":
    print(Solution().findMin([4,5,6,7,0,1,2]))