class Solution:
    def find3Numbers(self, arr):
        arr.sort()
        arr = sorted(set(arr))

        if len(arr) < 3:
            return 0
                
        return list(arr)[:3]

n1 = [1,2,1,1,3]
n2 = [1,1,3]
n3 = [104, 753, 852, 120, 676, 984]
n4 = [515, 519, 122]

sol = Solution()
print(sol.find3Numbers(n4))
