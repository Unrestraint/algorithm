"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。


示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        双指针 + 滑动窗口
        :type s: str
        :type t: str
        :rtype: str
        """
        l = 0 # 左
        r = 0 # 右
        # 用于统计 t 中字符在 s中出现的次数
        cnt = {}
        # 用于统计 t 中各字符个数
        chNum = {}
        for ch in t:
            chNum[ch] = chNum.get(ch, 0) + 1
        # t 中各字符个数，用于判断是否找到符合条件的字串
        chNumTemp = {**chNum}

        # 指针 b 先向右滑动，直至找到所有字符
        # a 滑动至第一个字符
        # cnt 统计 t 中字符出现的次数
        j = 0
        for i in range(0, len(s)):
            ch = s[i]
            if ch in chNum:
                cnt[ch] = cnt.get(ch, 0) + 1
                # 先找到第一个符合条件的子数组
                if ch in chNumTemp:
                    chNumTemp[ch] -= 1
                    if chNumTemp[ch] == 0:
                        del chNumTemp[ch]
                    if len(chNumTemp) == 0:
                        r = i
                # 已经找到所有的字符，窗口收缩
                if len(chNumTemp) == 0:
                    while j <= i:
                        if s[j] in chNum:
                            if cnt[s[j]] > chNum[s[j]]:
                                cnt[s[j]] -= 1
                                j += 1
                            else:
                                break
                        else:
                            j += 1
                    # 获取最小字符串
                    if i - j < r - l:
                        r = i
                        l = j

        # 数组不存在字串
        if len(chNumTemp) != 0:
            return ""

        return s[l: r+1]



if __name__ == "__main__":
    print(Solution().minWindow("bba","ba"))

"ADOBECODEBANC"
"ABC"

"cabwefgewcwaefgcf"
"cae"