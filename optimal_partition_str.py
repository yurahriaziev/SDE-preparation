class Solution:
    def partitionString(self, s: str) -> int:
        res = []
        sub_s = ''
        for i in s:
            if i not in sub_s:
                sub_s += i
            else:
                res.append(sub_s)
                sub_s = i
        res.append(sub_s)

        return len(res)

sol = Solution()
print(sol.partitionString('abacaba'))