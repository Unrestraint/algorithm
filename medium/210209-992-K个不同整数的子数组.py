"""
给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。
（例如，[1,2,3,1,2] 中有3个不同的整数：1，2，以及3。）
返回A中好子数组的数目。

示例 1：
输入：A = [1,2,1,2,3], K = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

示例 2：
输入：A = [1,2,1,3,4], K = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].

提示：
1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarrays-with-k-different-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        l = len(A)
        # key：A中的数字， value：该数字当前计数
        map = {}
        # 好子数组的个数
        c = 0
        # 慢指针
        j = 0
        # 快指针
        for i in range(0, len(A)):
            # 将当前数字放入计数器
            map[A[i]] = map.get(A[i], 0) + 1
            # map 中的数字数量小于 K，以下跳过，移动快指针计数。

            # 如果 map 中的数字数量大于 K，移动慢指针删除数字
            if len(map) > K:
                for k in range(j, i+1):
                    map[A[k]] = map.get(A[k], 0) - 1
                    if map[A[k]] <= 0:
                        del map[A[k]]
                    j += 1
                    if len(map) == K:
                        break
            # 如果map中的数量等于K，从慢指针开始遍历查找符合条件的数量
            if len(map) == K:
                sub_map = map.copy()
                for k in range(j, i+1):
                    if len(sub_map) == K:
                        c += 1
                    else:
                        break
                    sub_map[A[k]] = sub_map.get(A[k], 0) -1
                    if sub_map[A[k]] <= 0:
                        del sub_map[A[k]]

        return c


if __name__ == "__main__":
    print(Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3))
