"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
            寻找第 k 大的元素，最简单的做法就是排序后，取第 K 大的元素。
            优化解法：
            1. 构建大顶堆，堆大小为 k
            2. 变形快速排序方式，当列表分为两个子数组时，在 k 所在的子数组中按同样方式查找
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = k-1
        l = 0
        r = len(nums) - 1
        while l < r :
            # 快速排序，基准
            c = l
            for i in range(l + 1, r + 1):
                # 比 基准值大的全部交换到前面
                if nums[i] >= nums[c]:
                    t = nums[c]
                    nums[c] = nums[i]
                    c += 1
                    nums[i] = nums[c]
                    nums[c] = t
            if k == c:
                break
            # 缩小查找范围
            if k > c:
                l = c + 1
            else:
                r = c - 1
        return nums[k]

if __name__ == "__main__":
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))



